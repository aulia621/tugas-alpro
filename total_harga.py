harga = int (input('input harga barang :'))
qty = int (input('input jumlah barang :'))
total_harga = harga * qty
print('total harga = ', total_harga)
bayar = int(input('input pembayaran : '))
kembalian = bayar - total_harga
print('kembalian = ', kembalian)

