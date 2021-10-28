a = True
umum=0
tabungan=0

while(a):
    print("**Aplikasi Pencatatan Uang Digital**")
    print("**************")
    print("[1] Informasi Saldo")
    print("[2] Tambah Saldo")
    print("[3] Ambil Saldo")
    print("[4] Keluar")
    print("**************")
    option=int(input("Pilih Menu:"))
    if option==1:
        print("Saldo umum Anda saat ini adalah: Rp.",umum)
        print("Saldo tabungan Anda saat ini adalah: Rp.",tabungan)
        print("**************")
    elif option==2:
        print("[1] Umum")
        print("[2] Tabungan")
        option2=int(input("Pilih Penyimpanan:"))
        print("**************")
        if option2==1:
            option3=int(input("Nominal uang yang akan ditambahkan :"))
            umum=umum+option3
            print("Saldo umum Anda saat ini adalah:",umum)
        elif option2==2:
            option4=int(input("Nominal uang yang akan ditambahkan :"))
            tabungan=tabungan+option4
            print("Saldo umum Anda saat ini adalah:",tabungan)
    elif option==3:
        print("[1] Umum")
        print("[2] Tabungan")
        opsiambil=int(input("pilih salo yang akan diambil :"))
        if opsiambil==1:
            ambil=int(input("saldo yang akan diambil:"))
            umum=umum-ambil
            print("saldo anda saat ini adalah:",umum)
        elif opsiambil==2:
            ambil=int(input("saldo yang akan diambil:"))
            tabungan=tabungan-ambil
            print("saldo anda saat ini adalah:",tabungan)
    elif option==4:
        exit(0)
