#https://viewer.diagrams.net/index.html?target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Rollercoaster%201#R1VfbcpswEP0apk%2FJAAJfHmM7aR%2FSjlt3ps2jYm1ArUCukC%2Fk67sywqDgJM7Eub0w6Ggl7Z49uwKPjLPNZ0UX6VfJQHihzzYemXhhOIhCfBqgrICIkApIFGcVFDTAjN%2BCBX2LLjmDwjHUUgrNFy44l3kOc%2B1gVCm5ds1upHBPXdAEOsBsTkUX%2FcWZTm1YYb%2FBvwBP0vrkoDesZjJaG9tIipQyuW5B5NwjYyWlrt6yzRiE4a7mpVp3cc%2FszjEFuT5kwTQf3Pz8rmYwjVc%2FVmxzyf%2FJExtGocs6YGAYvx1KpVOZyJyK8wYdKbnMGZhdfRw1NpdSLhAMEPwDWpc2mXSpJUKpzoSdRYdV%2BdusP%2B2RsAauEDjxT%2F1%2BXCOTjT2jGpXt0RQUz0CDsmAVh3H%2BXnosVMilmsMDnNQyoyoB%2FYBdvEsiih8keqNKXKdAUM1Xrh%2FUyjDZ2dmlZ0rRsmWwkDzXRWvnqQHQwBYUIbagbD0FcdzOOr5UO9ajlmsNtFXGE1QyfGOVREHUVon%2FQQQSHUMgHQUEkSuAoe%2FuULllFzXKeKrQer3X15nlYkXF0rJje6tpbT2aoXBGid4m0w%2Bw52ceuehIU6Uyu15ilKN1yjXMFnSbzDVeT67A7GGgNGwe1kQ3h%2FWCoO%2ByVF9b6%2BauCHoWS1v3xN2ktdPe4vjpFJK3KNUj1lZ4YG3dk5eDa%2BtZJIcdnc7QYd2V4o7Y4HE53nAhxlJItV1LWAwDZtpeoZX8C62ZQXhNsDqPI2DiCjjco99wj36jl9Jv1KF2TPNPpgPg5yE8j%2BEj8EV8l6499T7ovyJd8T663gtZYb%2F%2Fvtiqz2%2FR9U12aMKAtcsFFTzJ8X2OgZsPipGhheNPwpmdyDhjVSuFgt%2FS6%2B1WppnaWxb3jUdePDF7YfcsqkZ6JJoHd%2B4gMuywTPaUcPhiLHev8SsoPjzN%2BC%2F7KM%2FRcXjGYfNfWH1cNT%2FX5Pw%2F
#Write a program that works out whether if a given number is an odd or even number
# > greater than
# < less than
# >=greater than
# <= less than 
# == equal to
# != not equal to
# modulo % is used ..it will divide the number and then it will give you the remainder of that number
number = int(input("Which number do you want to check? "))

if(number % 2 == 0):
    print(f"{number} is a Even Number")
else:
    print(f"{number} is a Odd Number")    