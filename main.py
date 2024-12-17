# Nokta çiftlerini tanımlayan liste
points = [(1, 2), (4, 6), (5, 8), (2, 1)]

# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5  # Öklid mesafesi formülü
    return distance

# Tüm mesafeleri hesaplayıp saklamak için bir liste
distances = []

# Tüm nokta çiftleri arasında mesafeleri hesaplayan döngü
for i in range(len(points)):
    for j in range(i + 1, len(points)):  # Aynı noktaları karşılaştırmamak için
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)  # Mesafeyi distances listesine ekle
        print(f"Mesafe {points[i]} ve {points[j]} arasında: {dist:.2f}")

# Minimum mesafeyi bulma
minimum_distance = min(distances)

# Sonucu ekrana yazdırma
print(f"\nEn küçük mesafe: {minimum_distance:.2f}")
