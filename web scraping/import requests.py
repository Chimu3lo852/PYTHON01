import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage

# --- CONFIGURACIÓN DE CORREO ---
REMITENTE = "felizronald6@gmail.com"
DESTINATARIO = "felizronald6@gmail.com"
CONTRASENA = "uihx tiyh ujyy gzwv"

def enviar_correo(asunto, cuerpo):
    msg = EmailMessage()
    msg["Subject"] = asunto
    msg["From"] = REMITENTE
    msg["To"] = DESTINATARIO
    msg.set_content(cuerpo)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(REMITENTE, CONTRASENA)
            smtp.send_message(msg)
            print("✅ Correo enviado correctamente.")
    except Exception as e:
        print(f"❌ Error al enviar el correo: {e}")

# --- SCRAPING ---
url = "https://quotes.toscrape.com/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.select("span.text")

    encontrado = False
    for quote in quotes:
        texto = quote.get_text()
        print("💬", texto)
        if "life" in texto.lower():
            encontrado = True
            break

    if encontrado:
        print("🚨 Frase con 'life' encontrada")
        enviar_correo("Frase encontrada", f"Se encontró una frase con la palabra 'life':\n\n{texto}")
    else:
        print("❌ No se encontró ninguna frase con 'life'")
else:
    print("❌ Falló la conexión:", response.status_code)
