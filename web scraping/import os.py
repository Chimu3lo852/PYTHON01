import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage

#  CONFIGURACIÓN 
REMITENTE = "felizronald6@gmail.com"            #  correo (Gmail)
DESTINATARIO = "felizronald6@gmail.co"     # Quien recibirá el mensaje
CONTRASENA = "zcoz hkbs hhhp uwmb"  #  contraseña de aplicación de Gmail

#  ENVÍO DE CORREO 
def enviar_correo(asunto: str, cuerpo: str) -> None:
    msg = EmailMessage()
    msg["Subject"] = asunto
    msg["From"] = REMITENTE
    msg["To"] = DESTINATARIO
    msg.set_content(cuerpo)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(REMITENTE, CONTRASENA)
            smtp.send_message(msg)
            print("📤 Correo enviado correctamente.")
    except Exception as e:
        print(f"❌ Error al enviar el correo: {e}")

#  SCRAPING DE AMAZON 
def buscar_producto():
    url = "https://www.amazon.com/s?k=ak680+max"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
    except Exception as e:
        print(f"❌ Error en la conexión: {e}")
        return

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        productos = soup.select("span.a-size-medium.a-color-base.a-text-normal")

        encontrado = False
        for producto in productos:
            nombre = producto.get_text().strip()
            print("🔎", nombre)
            if "AK680" in nombre.upper():
                encontrado = True
                break

        if encontrado:
            print("🚨 ¡El producto AK680 fue encontrado!")
            enviar_correo(
                asunto="¡AK680 disponible en Amazon!",
                cuerpo=f"Se encontró el teclado AK680 en Amazon. Mira aquí:\n{url}"
            )
        else:
            print("❌ El producto AK680 no se encontró.")
    else:
        print("❌ Falló el acceso a Amazon. Código:", response.status_code)

# --- EJECUCIÓN UNA SOLA VEZ PARA PRUEBA ---
buscar_producto()
