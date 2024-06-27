# Coordinate System

Bu projede, Python ile geliştirilmiş bir koordinat sistemi yer almaktadır.
Şu anki haliyle bundan ibaret olsa da uygulamanın ileri sürümlerinde nokta, doğru, üçgen gibi elemanlar eklenip düzlem üzerinde simüle edilebilir.


## Uygulamadan Görseller

![alt text](https://github.com/umutcanekinci/coordinate-system/blob/main/sample.png?raw=true)

## Başlangıç

### Gereksinimler

Projeyi çalıştırmak için aşağıdaki yazılımlara ihtiyacınız olacaktır:

- Python 3.x
- Gerekli kütüphaneler (aşağıda listelenmiştir)
    - pygame=2.5.2

### Kurulum

*Kurulum yapmadan derlenmiş edilmiş çalıştırılabilir uygulama ile devam etmek istiyorsanız kurulum aşaması atlayıp __main__.exe dosyasını çalıştırabilirsiniz.


Gerekli kütüphaneleri yüklemek için aşağıdaki adımları izleyin:

1. Bu projeyi klonlayın:
    ```sh
    git clone https://github.com/umutcanekinci/coordinate-system.git
    cd coordinate-system
    ```  

2. Sanal ortam oluşturun:
    ```sh
    python -m venv venv
    source venv/bin/activate # Windows kullanıyorsanız: venv\Scripts\activate
    ```

3. Gerekli paketleri yükleyin:
    ```sh
    pip install -r requirements.txt
    ```

### Çalıştırma

Oyunu çalıştırmak için şu komutu kullanın:
```sh
python __main__.py
```


Ya da Kurulum yapmadan derlenmiş edilmiş çalıştırılabilir uygulama ile devam etmek istiyorsanız kurulum aşaması atlayıp __main__.exe dosyasını çalıştırabilirsiniz.

### Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen şu adımları izleyin:

1. Bu depoyu fork'layın (sağ üstteki Fork butonuna tıklayın).

2. Fork'ladığınız depoyu yerel makinenize klonlayın:
```sh
git clone https://github.com/umutcanekinci/coordinate-system.git
cd coordinate-system
```

3. Yeni bir dal oluşturun (örn: feature/yenilik):
```sh
git checkout -b feature/yenilik
```

4. Değişikliklerinizi yapın ve commit edin:
```sh
git commit -am 'Yeni özellik ekledim'
```

5. Değişikliklerinizi dalınıza iterek GitHub'a gönderin:
```sh
git push origin feature/yenilik
```

6. Pull request oluşturun.

### Lisans

Bu proje MIT Lisansı ile lisanslanmıştır - detaylar için LICENSE dosyasına bakabilirsiniz.

### İletişim

Sorularınız veya önerileriniz için umutcannekinci@gmail.com üzerinden iletişime geçebilirsiniz.
