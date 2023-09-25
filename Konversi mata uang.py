print('Program Login Sederhana')
print('-----------------------')

nama_1 = input('masukan nama anda :')
nim_1 = input('masukan nim anda :')
print('\n--------DATA DI KONFIRMASI---------')

nama_2 = input('\nmasukan nama anda :')
nim_2 = input('masukan nim anda :')

if nama_2==nama_1 and nim_2==nim_1:
    print('---------------------------')
    print('Login Di Terima Selamat Datang ' + nama_1 + '..')
    print('---------------------------')
else:
    print('---------------------------')
    print('Login Di Tolak Silahkan Di coba lagi.. ')
    print('---------------------------')
    #
print("Program Konversi Rupiah Ke Mata Uang Asing")
#judul program

print("")
#membuat fungsi mata uang dunia
def mata_uang_dunia():
    print("Pilih Mata Uang Yang Akan Di Konversi")
    print(" 1. US Dollar (Rp.15.384,10)")
    print(" 2. Yen (Rp.103.550,00)")
    print(" 3. Ringgit Malaysia (Rp.3.283,05)")
    print(" 4. Selesai")

print("")

#kondisi awal variable
masukan=0
mata_uang=0
hasil=0

#kondisi whille
while True:
    mata_uang_dunia()
    pilihan=input("Masukan Pilihan:")
    pilihan=int(pilihan)

    if pilihan==1:
        masukan=input("Masukan Nominal:")
        masukan=int(masukan)
        print("")
        mata_uang=15.384
        hasil=masukan*mata_uang
        print(f" Rp {masukan} senilai dengan {hasil} $")
        print("")
        print('----------------------------------------')
    
    if pilihan==2:
        masukan=input("Masukan Nominal:")
        masukan=int(masukan)
        print("")
        mata_uang=103.550
        hasil=masukan*mata_uang
        print(f" Rp {masukan} senilai dengan {hasil} ¥")
        print("")
        print('----------------------------------------')
   
    if pilihan==3:
        masukan=input("Masukan Nominal:")
        masukan=int(masukan)
        print("")
        mata_uang=3.283
        hasil=masukan*mata_uang
        print(f" Rp {masukan} senilai dengan {hasil} Rm")
        print("")
        print('----------------------------------------')
   
    if pilihan==4:
        print("Program Selesai")
        break