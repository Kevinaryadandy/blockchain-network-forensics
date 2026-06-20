import os
import hashlib
import json
from datetime import datetime
from scapy.all import rdpcap

def get_pcap_metadata(file_path):

    if not os.path.exists(file_path):
        print(f"[Error] File {file_path} tidak ditemukan.")
        return None

    file_size = os.path.getsize(file_path)

    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    evidence_hash = sha256_hash.hexdigest()

    
    try:
        packets = rdpcap(file_path)
        packet_count = len(packets)
    except Exception as e:
        print(f"[Error] Gagal membaca paket dari {file_path}: {e}")
        packet_count = 0

    return {
        "file_name": os.path.basename(file_path),
        "packet_count": packet_count,
        "file_size": f"{file_size} Bytes",
        "evidence_hash": evidence_hash
    }

class Block:
    def __init__(self, index, timestamp, evidence_file, packet_count, evidence_hash, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.evidence_file = evidence_file
        self.packet_count = packet_count
        self.evidence_hash = evidence_hash
        self.previous_hash = previous_hash
        self.block_hash = self.calculate_block_hash()

    def calculate_block_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "evidence_file": self.evidence_file,
            "packet_count": self.packet_count,
            "evidence_hash": self.evidence_hash,
            "previous_hash": self.previous_hash
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Membuat Genesis Block sebagai awal mula rantai blockchain (Index 0).
        (Sesuai ketentuan pada Screenshot (765).png)
        """
        genesis_block = Block(
            index=0,
            timestamp=str(datetime.now()),
            evidence_file="Genesis Block",
            packet_count=0,
            evidence_hash="0",
            previous_hash="0"
        )
        self.chain.append(genesis_block)

    def get_latest_block(self):
        return self.chain[-1]

    def add_evidence_block(self, pcap_metadata):
        """
        Menambahkan evidence block baru berdasarkan data hasil analisis file PCAP.
        """
        latest_block = self.get_latest_block()
        new_block = Block(
            index=len(self.chain),
            timestamp=str(datetime.now()),
            evidence_file=pcap_metadata["file_name"],
            packet_count=pcap_metadata["packet_count"],
            evidence_hash=pcap_metadata["evidence_hash"],
            previous_hash=latest_block.block_hash
        )
        self.chain.append(new_block)

    def validate_blockchain(self):
        """
        Mengimplementasikan fungsi validasi untuk memverifikasi:
        - Kesesuaian Previous Hash
        - Integritas seluruh blockchain (re-calculate hash)
        (Sesuai ketentuan pada Screenshot (765).png & Screenshot (766).png)
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.block_hash != current_block.calculate_block_hash():
                return "INVALID (Data Integrity Compromised)"

            if current_block.previous_hash != previous_block.block_hash:
                return "INVALID (Chain Broken / Previous Hash Mismatch)"

        return "VALID"

    def display_chain(self):
        """
        Menampilkan isi blockchain secara terstruktur ke layar terminal.
        """
        for block in self.chain:
            print(f"==================================================")
            print(f"Index          : {block.index}")
            print(f"Timestamp      : {block.timestamp}")
            print(f"Evidence File  : {block.evidence_file}")
            print(f"Packet Count   : {block.packet_count}")
            print(f"Evidence Hash  : {block.evidence_hash}")
            print(f"Previous Hash  : {block.previous_hash}")
            print(f"Block Hash     : {block.block_hash}")
        print(f"==================================================")


if __name__ == "__main__":
    evidence_folder = "../evidence" 
    
    pcap_files = [
        "PCAP01_23040700094.pcap",
        "PCAP02_23040700094.pcap",
        "PCAP03_23040700094.pcap",
        "PCAP04_23040700094.pcap",
        "PCAP05_23040700094.pcap"
    ]

    print("=== TAHAP 1: Perhitungan Hash Bukti Digital (PCAP) ===")
    metadata_list = []
    
    for file_name in pcap_files:
        file_path = os.path.join(evidence_folder, file_name)
        
        metadata = get_pcap_metadata(file_path)
        
        if metadata:
            print(f"\n[+] Nama File   : {metadata['file_name']}")
            print(f"    Jumlah Paket: {metadata['packet_count']}")
            print(f"    Ukuran File : {metadata['file_size']}")
            print(f"    SHA-256     : {metadata['evidence_hash']}")
            metadata_list.append(metadata)
        else:
            print(f"[-] Skip {file_name} karena tidak ditemukan.")

    blockchain = Blockchain()

    print("\n=== TAHAP 2: Simulasi Memasukkan Metadata PCAP ke Blockchain ===")
    for meta in metadata_list:
        blockchain.add_evidence_block(meta)
    
    blockchain.display_chain()

    print("\n=== TAHAP 3: Validasi Blockchain ===")
    validation_result = blockchain.validate_blockchain()
    print(f"Blockchain Validation : {validation_result}")