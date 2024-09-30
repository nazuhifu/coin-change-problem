from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)


def minimumCoin(uangTotal, pecahan):
    hasil = []

    # Melakukan iterasi melalui setiap pecahan uang
    i = len(pecahan) - 1
    while (i >= 0):
        while (uangTotal >= pecahan[i]):
            uangTotal -= pecahan[i]
            hasil.append(pecahan[i])

        i -= 1

    # Cetak hasil
    print(f"\n{Fore.YELLOW}Pecahan yang digunakan:")
    for i in range(len(hasil)):
        print(f"{Fore.CYAN}{hasil[i]}", end=" ")

    print(f"\n\n{Fore.GREEN}Total pecahan yang digunakan: {len(hasil)}")


if __name__ == '__main__':
    print(f"{Fore.MAGENTA}{Style.BRIGHT}--- Tukar Uang ---")
    print(f"{Fore.MAGENTA}{'-' * 30}")

    total = int(input(f"{Fore.CYAN}Input uang yang ingin ditukar: "))

    print(f"\n{Fore.CYAN}Input pecahan uang yang tersedia")
    pecahan_input = input(f"{Fore.CYAN}(pisahkan dengan spasi): ")

    # Mengubah input pecahan menjadi list of integers
    pecahan = list(map(int, pecahan_input.split()))

    pecahan.sort()  # Mengurutkan pecahan dari kecil ke besar

    # Menampilkan jumlah minimal uang pecahan
    print(f"{Fore.MAGENTA}\n{'-' * 30}")
    print(f"{Fore.YELLOW}Jumlah minimal pecahan untuk {total}: ", end="")
    minimumCoin(total, pecahan)
