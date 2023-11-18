"""
baixando o módulo qrcode
"""
import qrcode

"""
Criaremos uma variável chamada qr que vai receber o método QRCode().
"""
qr = qrcode.QRCode( version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4 ) 

"""
Vamos usar o método add_data() para informar o conteúdo do qrcode
"""

qr.add_data('https://github.com/R0onald')

"""
Agora precisamos usar o método make() e informar o parâmetro fit=True
"""
qr.make(fit=True)

"""
método make_image(). Dentro desse método é possível configurar as cores do nosso QRCode.
"""
imagem = qr.make_image(fill_color='black', back_color='white') 

"""
salvando as informações corretamente 
"""
imagem.save('qrcode-gerado.png')
