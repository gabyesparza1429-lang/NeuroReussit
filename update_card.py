import re

with open("index.html", "r") as f:
    html = f.read()

# Buscar qué imagen existe exactamente para NeuroClarity
img_name = "NeuroClarity.png"

# Reconstruir la tarjeta 2 exactamente igual a la 1
tarjeta_neuroclarity = f'''<a href="https://neuroclarity.neuroreussit.com/" class="puerta-proyecto">
                <img src="./assets/{img_name}" alt="Logo NeuroClarity" class="logo-grande">
                <div class="pilar-title">NeuroClarity: Metodología para Mentes Diversas</div>
                <div class="pilar-description">
                    Desarrollamos soluciones digitales que reconen y valoran la neurodivergencia, adaptando la entrega de contenido para reducir la carga cognitiva y optimizar la comprensión. Nuestra tecnología es la herramienta clave para disminuir la brecha educativa, asegurando que ninguna forma de aprender sea un obstáculo para alcanzar la excelencia profesional.
                </div>
                <button class="btn-entrar" style="background: #B099CE;">Entrar</button>
            </a>'''

# Reemplazar la segunda tarjeta
partes = html.split('<a href=')
if len(partes) >= 3:
    # La tercera parte corresponde a la segunda tarjeta
    encabezado = partes[0] + '<a href=' + partes[1] + '<a href='
    resto = partes[2][partes[2].find('</a>') + 4:]
    html_final = encabezado + tarjeta_neuroclarity + resto
    with open("index.html", "w") as f:
        f.write(html_final)
