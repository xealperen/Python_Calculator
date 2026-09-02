gecerli = False
while not gecerli:

    def add(a,b):
        return a + b    #Toplama İşlemleri Burda Yapılıyor

    def subtract(a,b):
        return a - b    #Çıkarma İşlemleri Burda Yapılıyor

    def multiply(a,b):
        return a * b    #Çarpma İşlemleri Burda Yapılıyor

    def divide(a,b):
        if b == 0: #Sıfıra Bölme Hatası Burda Yakalanıyor
            raise ValueError("Cannot divide by zero.") #Sıfıra Bölme Hatası Burda Yakalanıyor
        return a / b    #Bölme İşlemleri Burda Yapılıyor

    def exit():
        print("Exiting the program.") #Programdan Çıkış Burda Yapılıyor
        quit() #Programdan Çıkış Burda Yapılıyor

    def main():     #Seçim İşlemleri Burda Yapılıyor
        print("Simple Calculator") #Hesap Makinesi Başlığı Burda Yazılıyor
        print("1. Add")              #toplama İşlemi Seçeneği Burda Yazılıyor
        print("2. Subtract")         #çıkarma İşlemi Seçeneği Burda Yazılıyor
        print("3. Multiply")         #çarpma İşlemi Seçeneği Burda Yazılıyor
        print("4. Divide")           #bölme İşlemi Seçeneği Burda Yazılıyor
        print("5. Exit")             #çıkış İşlemi Seçeneği Burda Yazılıyor

        choice = input("Enter choice (1/2/3/4/5): ")  #Hangi İşlemi Yapmak İstediğinizi Seçiyorsunuz

        if choice == '5':
            exit() #Programdan Çıkış Burda Yapılıyor
            
        num1 = int(input("Enter first number: ")) #İlk Sayıyı Giriyorsunuz
        num2 = int(input("Enter second number: ")) #İkinci Sayıyı Giriyorsunuz
        if choice == '1':
                print("Output:", add(num1, num2))
        elif choice == '2':
                print("Output:", subtract(num1, num2))
        elif choice == '3':
                print("Output:", multiply(num1, num2))
        elif choice == '4':
                print("Output:", divide(num1, num2))
        elif choice == '5':
                exit()
        else:
                print("Invalid choice.")

    if __name__ == "__main__": #İşlem Başlatılıyor
        main() #İşlem Başlatılıyor