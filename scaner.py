import cv2
import pyzbar.pyzbar as pyzbar
import csv

def read_datamatrix(image_path, output_file):
    # Загрузка изображения
    image = cv2.imread(image_path)

    # Преобразование изображения в черно-белый формат
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Декодирование кодов DataMatrix
    barcodes = pyzbar.decode(gray)

    # Считывание содержимого кодов DataMatrix
    decoded_data = []
    for barcode in barcodes:
        data = barcode.data.decode('utf-8')
        decoded_data.append(data)

    # Вывод распознанных кодов на экран
    print("Распознанные коды DataMatrix:")
    for data in decoded_data:
        print(data)

    # Сохранение результатов в файл CSV
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Распознанный код DataMatrix'])
        for data in decoded_data:
            writer.writerow([data])

    print("Результаты сохранены в файл", output_file)

# Пример использования
image_path = 'll.png'
output_file = 'output.csv'
read_datamatrix(image_path, output_file)