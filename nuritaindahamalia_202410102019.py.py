total= 0
command = "y"
kesalahan_karakter= list()
while True:
        if command == "y":
            jumlah_barang= int (input("entrikan jumlah barang yang dibeli: "))
            harga_barang= int(input("entrikan harga barang satuan: "))
            total+= jumlah_barang*harga_barang
        elif command=="t":
            print("total pembayaran: Rp.",'{:,}'. format(total))
            break
        else:
            kesalahan_karakter.append(command)
        command= input("apakah ada lagi barang yang akan dientrikan lagi?[y/t]")

for a in range(len(kesalahan_karakter)):
      print('Karakter salah indeks ',str(a), 'adalah:',kesalahan_karakter[a])
