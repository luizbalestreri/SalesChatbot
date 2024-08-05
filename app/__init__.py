from flask import Flask
from app.models import Product
import os
from .database import db

def create_app():
    app = Flask(__name__)

    # Configure the PostgreSQL database connection
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    with app.app_context():
        from .models import Product, Usuario, Sessions
        db.create_all()
        if not Product.query.first():
            populate_database()

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

def populate_database():
    base_url = "www.loja.com/sku/"
    products = [
        {
            'sku': 'SKU001',
            'name': 'NovoPhone X12',
            'quantity': 100,
            'description': 'O NovoPhone X12 é um smartphone de última geração, equipado com uma tela AMOLED de 6.5 polegadas, câmera traseira tripla de 64MP, 12MP e 5MP, e uma câmera frontal de 32MP. Sua bateria de 5000mAh garante um dia inteiro de uso com uma única carga. Ele também possui um processador octa-core, 8GB de RAM e 128GB de armazenamento interno, expansível via cartão microSD. Ideal para quem busca desempenho e qualidade de imagem excepcionais.',
            'price': 3499.00,
            'category': 'Smartphone'
        },
        {
            'sku': 'SKU002',
            'name': 'UltraBook Pro 15',
            'quantity': 100,
            'description': 'O UltraBook Pro 15 é um laptop poderoso e sofisticado, perfeito para tarefas exigentes como edição de vídeo e design gráfico. Possui uma tela de 15.6 polegadas com resolução 4K, processador Intel Core i7 de 10ª geração, 16GB de RAM e 1TB de SSD. Inclui uma placa gráfica dedicada NVIDIA GeForce GTX 1650, teclado retroiluminado e bateria de longa duração de até 10 horas. Um equipamento completo para profissionais criativos.',
            'price': 7999.00,
            'category': 'Laptop'
        },
        {
            'sku': 'SKU003',
            'name': 'TimeWatch S2',
            'quantity': 100,
            'description': 'O TimeWatch S2 é um smartwatch elegante e funcional, com uma tela AMOLED de 1.4 polegadas e resistência à água até 50 metros de profundidade. Ele oferece monitoramento de frequência cardíaca, níveis de oxigênio no sangue (SpO2), e uma variedade de modos de esporte. Possui GPS integrado, notificações inteligentes, e uma bateria que dura até 7 dias. Ideal para quem busca um companheiro para a vida fitness e o dia a dia.',
            'price': 1299.00,
            'category': 'Smartwatch'
        },
        {
            'sku': 'SKU004',
            'name': 'TabMaster 10',
            'quantity': 100,
            'description': 'O TabMaster 10 é um tablet versátil com uma tela de 10.1 polegadas Full HD, perfeito para entretenimento e produtividade. Equipado com um processador octa-core, 4GB de RAM e 64GB de armazenamento interno, expansível até 256GB com cartão microSD. Possui câmeras de 8MP (traseira) e 5MP (frontal), além de bateria de 6000mAh que proporciona até 12 horas de uso contínuo. Perfeito para assistir filmes, estudar ou trabalhar remotamente.',
            'price': 2499.00,
            'category': 'Tablet'
        },
        {
            'sku': 'SKU005',
            'name': 'SoundBuds Plus',
            'quantity': 100,
            'description': 'Os SoundBuds Plus são fones de ouvido sem fio que oferecem uma experiência sonora imersiva com drivers de alta qualidade e tecnologia de cancelamento de ruído ativo (ANC). Possuem até 8 horas de autonomia de bateria com uma única carga, e o estojo de carregamento portátil proporciona até 24 horas adicionais de uso. Confortáveis e leves, são ideais para uso diário e atividades físicas.',
            'price': 399.00,
            'category': 'Fone de Ouvido'
        },
        {
            'sku': 'SKU006',
            'name': 'PhotoSnap DSLR',
            'quantity': 100,
            'description': 'A PhotoSnap DSLR é uma câmera profissional que oferece qualidade de imagem superior com um sensor de 24.2MP e capacidade de gravação de vídeo em 4K. Possui uma lente intercambiável 18-55mm, estabilização de imagem, e uma tela LCD articulada de 3 polegadas. Inclui conectividade Wi-Fi e Bluetooth para compartilhamento rápido de fotos. Perfeita para fotógrafos que buscam desempenho e versatilidade.',
            'price': 4499.00,
            'category': 'Câmera'
        },
        {
            'sku': 'SKU007',
            'name': 'VisionScreen 55" 4K',
            'quantity': 100,
            'description': 'A VisionScreen 55" 4K é uma Smart TV que proporciona uma experiência visual incrível com sua resolução 4K Ultra HD e suporte a HDR10+. Possui uma tela de 55 polegadas, som Dolby Atmos, e sistema operacional integrado para acesso a aplicativos de streaming como Netflix, YouTube e Amazon Prime Video. Conta com conectividade Wi-Fi e Bluetooth, além de múltiplas entradas HDMI e USB.',
            'price': 3999.00,
            'category': 'Smart TV'
        },
        {
            'sku': 'SKU008',
            'name': 'GameBox X',
            'quantity': 100,
            'description': 'O GameBox X é um console de videogame de última geração, projetado para oferecer jogos com gráficos impressionantes e tempos de carregamento rápidos. Equipado com um processador octa-core, 16GB de RAM e 1TB de armazenamento SSD. Suporta resolução 4K e taxa de atualização de até 120Hz, proporcionando uma experiência de jogo fluida e envolvente. Inclui um controle ergonômico e compatibilidade com uma vasta biblioteca de jogos.',
            'price': 2999.00,
            'category': 'Console de Videogame'
        }
    ]

    for product in products:
        product['link_produto'] = f"{base_url}{product['sku']}"
        p = Product(**product)
        db.session.add(p)
    db.session.commit()