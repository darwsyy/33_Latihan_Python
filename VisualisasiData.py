import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = {
    "Nama": ["Tangguh", "Budi", "Darwisy", "Andi"],
    "Nilai_Tugas": [85, 70, 90, 60],
    "Nilai_Ujian": [90, 75, 95, 65]
}


df = pd.DataFrame(data)


df["Rata_Rata"] = np.mean([df["Nilai_Tugas"], df["Nilai_Ujian"]], axis=0)

print("=== TABEL DATA SISWA ===")
print(df)

plt.bar(df["Nama"], df["Rata_Rata"], color="skyblue", edgecolor="black")

plt.title("Grafik Rata-Rata Nilai Siswa")
plt.xlabel("Nama Siswa")
plt.ylabel("Rata-Rata Nilai")
plt.ylim(0, 100) 

plt.show()