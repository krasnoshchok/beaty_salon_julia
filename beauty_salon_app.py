from flask import Flask, render_template_string, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'julia-salon-secret-key-2025'

# Translations dictionary
translations = {
    'pl': {
        'site_title': 'Salon Piękności Julia',
        'nav_home': 'Strona Główna',
        'nav_gallery': 'Galeria',
        'nav_contact': 'Kontakt',
        'home_title': 'Witaj w Salonie Piękności "Julia"',
        'home_subtitle': 'Twoje piękno jest naszą pasją',
        'home_description': 'Odkryj prawdziwe piękno w naszym ekskluzywnym salonie. Oferujemy profesjonalne usługi kosmetyczne, stylizację włosów, manicure i wiele więcej. Nasze doświadczone stylistki pomogą Ci wyglądać i czuć się wspaniale.',
        'home_services': 'Nasze Usługi:',
        'service_hair': '💇‍♀️ Stylizacja włosów',
        'service_makeup': '💄 Makijaż profesjonalny',
        'service_nails': '💅 Manicure i pedicure',
        'service_facial': '✨ Zabiegi na twarz',
        'service_massage': '🌸 Masaże relaksacyjne',
        'gallery_title': 'Nasza Galeria',
        'gallery_subtitle': 'Zobacz nasze prace',
        'contact_title': 'Skontaktuj się z nami',
        'contact_subtitle': 'Umów wizytę już dziś',
        'contact_phone': 'Telefon: +48 123 456 789',
        'contact_email': 'Email: kontakt@julia-salon.pl',
        'contact_address': 'Adres: ul. Piękna 15, 00-001 Warszawa',
        'contact_info': 'Nasze kontakty',
        'contact_hours': 'Godziny otwarcia:',
        'hours_weekdays': 'Pon-Pt: 9:00 - 19:00',
        'hours_saturday': 'Sobota: 9:00 - 17:00',
        'hours_sunday': 'Niedziela: Zamknięte',
        'footer_text': 'Wszystkie prawa zastrzeżone.'
    },
    'ua': {
        'site_title': 'Салон Краси Юлія',
        'nav_home': 'Головна',
        'nav_gallery': 'Галерея',
        'nav_contact': 'Контакти',
        'home_title': 'Ласкаво просимо до Салону Краси "Юлія"',
        'home_subtitle': 'Ваша краса - наша пристрасть',
        'home_description': 'Відкрийте справжню красу в нашому ексклюзивному салоні. Ми пропонуємо професійні косметичні послуги, стилізацію волосся, манікюр та багато іншого. Наші досвідчені стилісти допоможуть вам виглядати і почуватися чудово.',
        'home_services': 'Наші Послуги:',
        'service_hair': '💇‍♀️ Стилізація волосся',
        'service_makeup': '💄 Професійний макіяж',
        'service_nails': '💅 Манікюр і педикюр',
        'service_facial': '✨ Процедури для обличчя',
        'service_massage': '🌸 Релаксуючий масаж',
        'gallery_title': 'Наша Галерея',
        'gallery_subtitle': 'Подивіться на наші роботи',
        'contact_title': 'Зв\'яжіться з нами',
        'contact_subtitle': 'Запишіться на прийом сьогодні',
        'contact_phone': 'Телефон: +48 123 456 789',
        'contact_email': 'Email: kontakt@julia-salon.pl',
        'contact_address': 'Адреса: вул. Пєкна 15, 00-001 Варшава',
        'contact_hours': 'Години роботи:',
        'contact_info': 'Наші контакти:',
        'hours_weekdays': 'Пн-Пт: 9:00 - 19:00',
        'hours_saturday': 'Субота: 9:00 - 17:00',
        'hours_sunday': 'Неділя: Зачинено',
        'footer_text': 'Всі права захищені.'
    },
    'en': {
        'site_title': 'Julia Beauty Salon',
        'nav_home': 'Home',
        'nav_gallery': 'Gallery',
        'nav_contact': 'Contact',
        'home_title': 'Welcome to "Julia" Beauty Salon',
        'home_subtitle': 'Your beauty is our passion',
        'home_description': 'Discover true beauty at our exclusive salon. We offer professional cosmetic services, hair styling, manicures and much more. Our experienced stylists will help you look and feel amazing.',
        'home_services': 'Our Services:',
        'service_hair': '💇‍♀️ Hair styling',
        'service_makeup': '💄 Professional makeup',
        'service_nails': '💅 Manicure & pedicure',
        'service_facial': '✨ Facial treatments',
        'service_massage': '🌸 Relaxing massage',
        'gallery_title': 'Our Gallery',
        'gallery_subtitle': 'See our work',
        'contact_title': 'Contact Us',
        'contact_subtitle': 'Book your appointment today',
        'contact_phone': 'Phone: +48 123 456 789',
        'contact_email': 'Email: kontakt@julia-salon.pl',
        'contact_address': 'Address: ul. Piękna 15, 00-001 Warsaw',
        'contact_info': 'Our contacts:',
        'contact_hours': 'Opening hours:',
        'hours_weekdays': 'Mon-Fri: 9:00 - 19:00',
        'hours_saturday': 'Saturday: 9:00 - 17:00',
        'hours_sunday': 'Sunday: Closed',
        'footer_text': 'All rights reserved.'
    }
}


def get_language():
    return session.get('language', 'pl')


def get_text(key):
    lang = get_language()
    return translations[lang].get(key, key)


@app.route('/set_language/<language>')
def set_language(language):
    if language in translations:
        session['language'] = language
    return redirect(url_for('home'))


# Main page with all sections
@app.route('/')
def home():
    template = '''
<!DOCTYPE html>
<html lang="{{ get_language() }}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ get_text('site_title') }}</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #0d1b2a 0%, #1b263b 25%, #2d3748 50%, #4a5568 75%, #2d3748 100%);
            background-attachment: fixed;
            color: #ffffff;
            min-height: 100vh;
            line-height: 1.6;
            overflow-x: hidden;
        }

        /* Animated background particles */
        .bg-particles {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: -1;
        }

        .particle {
            position: absolute;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 50%;
            animation: float 6s ease-in-out infinite;
        }

        .particle:nth-child(1) { width: 4px; height: 4px; top: 10%; left: 20%; animation-delay: 0s; }
        .particle:nth-child(2) { width: 6px; height: 6px; top: 20%; left: 80%; animation-delay: 1s; }
        .particle:nth-child(3) { width: 3px; height: 3px; top: 60%; left: 10%; animation-delay: 2s; }
        .particle:nth-child(4) { width: 5px; height: 5px; top: 80%; left: 90%; animation-delay: 3s; }
        .particle:nth-child(5) { width: 4px; height: 4px; top: 40%; left: 60%; animation-delay: 4s; }

        @keyframes float {
            0%, 100% { transform: translateY(0px) rotate(0deg); opacity: 0.7; }
            50% { transform: translateY(-20px) rotate(180deg); opacity: 1; }
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        /* Header */
        header {
            background: rgba(13, 27, 42, 0.95);
            backdrop-filter: blur(20px);
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            border-bottom: 2px solid rgba(255, 105, 180, 0.3);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        }

        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 0;
            flex-wrap: wrap;
            gap: 1rem;
        }

        .logo {
            font-size: 2.5rem;
            font-weight: bold;
            background: linear-gradient(45deg, #ff69b4, #ffd700, #ff1493, #da70d6);
            background-size: 400% 400%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: gradientShift 3s ease-in-out infinite;
            text-shadow: 0 0 30px rgba(255, 105, 180, 0.5);
        }

        @keyframes gradientShift {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }

        .nav-links {
            display: flex;
            list-style: none;
            gap: 2rem;
            flex-wrap: wrap;
        }

        .nav-links a {
            color: #ffffff;
            text-decoration: none;
            transition: all 0.4s ease;
            padding: 0.8rem 1.5rem;
            border-radius: 30px;
            border: 2px solid transparent;
            position: relative;
            overflow: hidden;
        }

        .nav-links a:hover {
            box-shadow: 0 8px 25px rgba(255, 105, 180, 0.4);
            border-color: #ff69b4;
        }

        .language-switcher {
            display: flex;
            gap: 0.5rem;
        }

        .language-switcher a {
            padding: 0.8rem 1.2rem;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            color: #ffffff;
            text-decoration: none;
            font-size: 0.9rem;
            transition: all 0.4s ease;
            border: 2px solid transparent;
            backdrop-filter: blur(10px);
        }

        .language-switcher a:hover {
            background: rgba(255, 105, 180, 0.3);
            border-color: #ff69b4;
            transform: scale(1.05);
        }

        .language-switcher a.active {
            background: linear-gradient(45deg, #ff69b4, #da70d6);
            border-color: #ffd700;
            box-shadow: 0 5px 15px rgba(255, 105, 180, 0.4);
        }

        /* Main content */
        main {
            margin-top: 100px;
        }

        .section {
            min-height: 100vh;
            padding: 4rem 0;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
        }

        .section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(255, 255, 255, 0.02);
            border-radius: 30px;
            margin: 2rem;
            z-index: -1;
            backdrop-filter: blur(10px);
        }

        @keyframes rotate {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }

        .content-section {
            background: rgba(255, 255, 255, 0.08);
            padding: 4rem;
            margin: 2rem 0;
            border-radius: 30px;
            backdrop-filter: blur(20px);
            border: 2px solid rgba(255, 105, 180, 0.2);
            width: 100%;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            position: relative;
            overflow: hidden;
        }

        .content-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: linear-gradient(90deg, transparent, #ff69b4, #ffd700, #ff1493, transparent);
            animation: shimmer 3s ease-in-out infinite;
        }

        @keyframes shimmer {
            0%, 100% { opacity: 0.5; }
            50% { opacity: 1; }
        }

        .section-title {
            font-size: 3rem;
            text-align: center;
            margin-bottom: 3rem;
            background: linear-gradient(45deg, #ff69b4, #ffd700, #ff1493);
            background-size: 200% 200%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: gradientShift 2s ease-in-out infinite;
            position: relative;
        }

        .section-title::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
            width: 100px;
            height: 3px;
            background: linear-gradient(45deg, #ff69b4, #ffd700);
            border-radius: 2px;
        }

        .services-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2.5rem;
            margin-top: 3rem;
        }

        .service-card {
            background: rgba(255, 255, 255, 0.12);
            padding: 3rem 2rem;
            border-radius: 25px;
            text-align: center;
            transition: all 0.5s ease;
            border: 2px solid rgba(255, 105, 180, 0.2);
            position: relative;
            overflow: hidden;
            backdrop-filter: blur(15px);
            height: 200px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .service-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(45deg, rgba(255, 105, 180, 0.2), rgba(218, 112, 214, 0.2));
            transition: left 0.5s ease;
            z-index: -1;
        }

        .service-card:hover::before {
            left: 0;
        }

        .service-card:hover {
            transform: translateY(-10px) scale(1.02);
            border-color: #ff69b4;
            box-shadow: 0 25px 50px rgba(255, 105, 180, 0.3);
        }

        .service-card h3 {
            font-size: 1.3rem;
            color: #ffffff;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
        }

        /* Gallery styles */
        .gallery-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2.5rem;
            margin-top: 3rem;
        }

        .gallery-item {
            height: 280px;
            border-radius: 25px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
            color: white;
            transition: all 0.5s ease;
            position: relative;
            overflow: hidden;
            cursor: pointer;
            border: 2px solid rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(10px);
            background-size: cover;
            background-position: center;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.8);
        }

        .gallery-item::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0, 0, 0, 0.4);
            transition: all 0.5s ease;
        }

        .gallery-item:hover::before {
            background: rgba(0, 0, 0, 0.2);
        }

        .gallery-item:hover {
            transform: scale(1.05) translateY(-5px);
            border-color: #ff69b4;
            box-shadow: 0 25px 50px rgba(255, 105, 180, 0.4);
        }

        .gallery-item:nth-child(1) {
            background: linear-gradient(45deg, #ff69b4, #ff1493),
                        url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="20" cy="20" r="2" fill="white" opacity="0.3"/><circle cx="80" cy="40" r="1.5" fill="white" opacity="0.4"/><circle cx="60" cy="80" r="1" fill="white" opacity="0.5"/></svg>');
        }

        .gallery-item:nth-child(2) {
            background: linear-gradient(45deg, #da70d6, #ff69b4),
                        url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="30" cy="70" r="2" fill="white" opacity="0.3"/><circle cx="70" cy="20" r="1.5" fill="white" opacity="0.4"/></svg>');
        }

        .gallery-item:nth-child(3) {
            background: linear-gradient(45deg, #ffd700, #ff69b4),
                        url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="40" cy="30" r="1.5" fill="white" opacity="0.4"/><circle cx="20" cy="80" r="2" fill="white" opacity="0.3"/></svg>');
        }

        .gallery-item:nth-child(4) {
            background: linear-gradient(45deg, #9370db, #da70d6);
        }

        .gallery-item:nth-child(5) {
            background: linear-gradient(45deg, #ff1493, #ffd700);
        }

        .gallery-item:nth-child(6) {
            background: linear-gradient(45deg, #4169e1, #ff69b4);
        }

        .gallery-item:nth-child(7) {
            background: linear-gradient(45deg, #ff69b4, #9370db);
        }

        .gallery-item:nth-child(8) {
            background: linear-gradient(45deg, #ffd700, #ff1493);
        }

        .gallery-item:nth-child(9) {
            background: linear-gradient(45deg, #da70d6, #4169e1);
        }

        /* Modal styles */
        .modal {
            display: none;
            position: fixed;
            z-index: 2000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.9);
            backdrop-filter: blur(10px);
            animation: fadeIn 0.3s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        .modal-content {
            position: relative;
            background: linear-gradient(45deg, #ff69b4, #da70d6);
            margin: 5% auto;
            padding: 0;
            width: 90%;
            max-width: 700px;
            border-radius: 25px;
            box-shadow: 0 30px 80px rgba(255, 105, 180, 0.5);
            animation: slideIn 0.4s ease;
        }

        @keyframes slideIn {
            from { transform: translateY(-50px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }

        .modal-image {
            width: 100%;
            height: 400px;
            border-radius: 25px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            color: white;
            text-shadow: 0 2px 20px rgba(0, 0, 0, 0.8);
        }

        .close {
            position: absolute;
            top: 15px;
            right: 25px;
            color: #ffffff;
            font-size: 35px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            background: rgba(0, 0, 0, 0.5);
            width: 45px;
            height: 45px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .close:hover {
            background: rgba(255, 105, 180, 0.8);
            transform: scale(1.1);
        }

        .contact-info {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 2.5rem;
            margin-top: 3rem;
        }

        .contact-card {
            background: rgba(255, 255, 255, 0.12);
            padding: 3rem;
            border-radius: 25px;
            border: 2px solid rgba(255, 105, 180, 0.2);
            transition: all 0.5s ease;
            backdrop-filter: blur(15px);
            height: 280px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .contact-card:hover {
            transform: translateY(-10px);
            border-color: #ff69b4;
            box-shadow: 0 25px 50px rgba(255, 105, 180, 0.3);
        }

        .contact-card h3 {
            color: #ffd700;
            margin-bottom: 1.5rem;
            font-size: 1.3rem;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
        }

        .contact-card p {
            margin-bottom: 0.8rem;
            color: #e2e8f0;
            font-size: 1.1rem;
        }

        /* Footer */
        footer {
            background: rgba(13, 27, 42, 0.95);
            text-align: center;
            padding: 3rem 0;
            border-top: 2px solid rgba(255, 105, 180, 0.3);
            backdrop-filter: blur(20px);
            margin-top: 2rem;
        }

        footer p {
            color: #e2e8f0;
            font-size: 1.1rem;
        }

        /* Responsive */
        @media (max-width: 768px) {
            nav {
                flex-direction: column;
                align-items: center;
                padding: 1.5rem 0;
            }

            .nav-links {
                gap: 1rem;
                justify-content: center;
            }

            .hero h1 {
                font-size: 2.8rem;
            }

            .section-title {
                font-size: 2.2rem;
            }

            .content-section {
                padding: 2.5rem;
                margin: 1rem 0;
            }

            .section {
                min-height: auto;
                padding: 2rem 0;
            }

            main {
                margin-top: 140px;
            }

            .services-grid, .gallery-grid {
                grid-template-columns: 1fr;
                gap: 2rem;
            }

            .contact-info {
                grid-template-columns: 1fr;
            }

            .gallery-item, .service-card, .contact-card {
                height: 220px;
            }
        }

        @media (max-width: 480px) {
            .language-switcher {
                flex-wrap: wrap;
                justify-content: center;
            }

            .hero h1 {
                font-size: 2.2rem;
            }

            .hero p {
                font-size: 1.2rem;
            }

            .content-section {
                padding: 2rem;
            }

            .modal-content {
                width: 95%;
                margin: 10% auto;
            }
        }
    </style>
</head>
<body>
    <div class="bg-particles">
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
    </div>

    <header>
        <nav class="container">
            <div class="logo">Julia</div>
            <ul class="nav-links">
                <li><a href="#home">{{ get_text('nav_home') }}</a></li>
                <li><a href="#contact">{{ get_text('nav_contact') }}</a></li>
                <li><a href="#gallery">{{ get_text('nav_gallery') }}</a></li>
            </ul>
            <div class="language-switcher">
                <a href="/set_language/pl" class="{{ 'active' if get_language() == 'pl' else '' }}">PL</a>
                <a href="/set_language/ua" class="{{ 'active' if get_language() == 'ua' else '' }}">UA</a>
                <a href="/set_language/en" class="{{ 'active' if get_language() == 'en' else '' }}">EN</a>
            </div>
        </nav>
    </header>

    <main>
        <!-- Home Section -->

        <section id="home" class="section">
            <div class="container">
                <div class="content-section">

                    <p style="font-size: 1.2rem; margin-bottom: 2.5rem; text-align: center; color: #e2e8f0;">{{ get_text('home_description') }}</p>

                    <h2 class="section-title">{{ get_text('home_services') }}</h2>
                    <div class="services-grid">
                        <div class="service-card">
                            <h3>{{ get_text('service_hair') }}</h3>
                        </div>
                        <div class="service-card">
                            <h3>{{ get_text('service_makeup') }}</h3>
                        </div>
                        <div class="service-card">
                            <h3>{{ get_text('service_nails') }}</h3>
                        </div>
                    </div>

                    <div style="text-align: center; padding: 2rem 0 3rem 0;">
                        <h1 style="font-size: 4rem; margin-bottom: 1.5rem; background: linear-gradient(45deg, #ff69b4, #ffd700, #ff1493, #da70d6); background-size: 400% 400%; -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; animation: gradientShift 3s ease-in-out infinite; text-shadow: 0 0 50px rgba(255, 105, 180, 0.5);">{{ get_text('home_title') }}</h1>
                        <p style="font-size: 1.5rem; color: #e2e8f0; text-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);">{{ get_text('home_subtitle') }}</p>
                    </div>
                </div>
            </div>
        </section>

    <!-- Contact Section -->
            <section id="contact" class="section">
                <div class="container">
                    <div class="content-section">
                        <h2 class="section-title">{{ get_text('contact_title') }}</h2>
                        <p style="text-align: center; font-size: 1.2rem; margin-bottom: 2.5rem; color: #e2e8f0;">{{ get_text('contact_subtitle') }}</p>

                        <div class="contact-info">
                            <div class="contact-card">
                                <h3>📞 {{ get_text('contact_info') }}</h3>
                                <p>{{ get_text('contact_phone') }}</p>
                                <p>{{ get_text('contact_email') }}</p>
                                <p>{{ get_text('contact_address') }}</p>
                            </div>
                            <div class="contact-card">
                                <h3>🕒 {{ get_text('contact_hours') }}</h3>
                                <p>{{ get_text('hours_weekdays') }}</p>
                                <p>{{ get_text('hours_saturday') }}</p>
                                <p>{{ get_text('hours_sunday') }}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>


            <!-- Gallery Section -->
            <section id="gallery" class="section">
                <div class="container">
                    <div class="content-section">
                        <h2 class="section-title">{{ get_text('gallery_title') }}</h2>
                        <p style="text-align: center; font-size: 1.2rem; margin-bottom: 2.5rem; color: #e2e8f0;">{{ get_text('gallery_subtitle') }}</p>

                        <div class="gallery-grid">
                            <div class="gallery-item" onclick="openModal('modal1')">
                                <span>💇‍♀️ Стилізація волосся - Елегантна зачіска</span>
                            </div>
                            <div class="gallery-item" onclick="openModal('modal2')">
                                <span>💄 Професійний макіяж - Вечірній образ</span>
                            </div>
                            <div class="gallery-item" onclick="openModal('modal3')">
                                <span>💅 Французький манікюр - Класичний стиль</span>
                            </div>
                            <div class="gallery-item" onclick="openModal('modal4')">
                                <span>💇‍♀️ Омбре - Градієнтне забарвлення</span>
                            </div>
                            <div class="gallery-item" onclick="openModal('modal5')">
                                <span>💄 Денний макіяж - Природна краса</span>
                            </div>
                            <div class="gallery-item" onclick="openModal('modal6')">
                                <span>✨ Догляд за обличчям - Очищення пор</span>
                            </div>
                            <div class="gallery-item" onclick="openModal('modal7')">
                                <span>💇‍♀️ Кучеряве волосся - Об'ємна укладка</span>
                            </div>
                            <div class="gallery-item" onclick="openModal('modal8')">
                                <span>💅 Арт-дизайн нігтів - Творчий підхід</span>
                            </div>
                            <div class="gallery-item" onclick="openModal('modal9')">
                                <span>💄 Весільний макіяж - Особливий день</span>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

        </main>

        <!-- Modals for gallery images -->
        <div id="modal1" class="modal" onclick="closeModal('modal1')">
            <div class="modal-content" onclick="event.stopPropagation()">
                <span class="close" onclick="closeModal('modal1')">&times;</span>
                <div class="modal-image" style="background: linear-gradient(45deg, #ff69b4, #ff1493);">
                    <div style="text-align: center;">
                        <h3 style="margin-bottom: 1rem;">💇‍♀️ Стилізація волосся</h3>
                        <p>Елегантна зачіска для особливих подій</p>
                    </div>
                </div>
            </div>
        </div>

        <div id="modal2" class="modal" onclick="closeModal('modal2')">
            <div class="modal-content" onclick="event.stopPropagation()">
                <span class="close" onclick="closeModal('modal2')">&times;</span>
                <div class="modal-image" style="background: linear-gradient(45deg, #da70d6, #ff69b4);">
                    <div style="text-align: center;">
                        <h3 style="margin-bottom: 1rem;">💄 Професійний макіяж</h3>
                        <p>Вечірній образ для особливих моментів</p>
                    </div>
                </div>
            </div>
        </div>

        <div id="modal3" class="modal" onclick="closeModal('modal3')">
            <div class="modal-content" onclick="event.stopPropagation()">
                <span class="close" onclick="closeModal('modal3')">&times;</span>
                <div class="modal-image" style="background: linear-gradient(45deg, #ffd700, #ff69b4);">
                    <div style="text-align: center;">
                        <h3 style="margin-bottom: 1rem;">💅 Французький манікюр</h3>
                        <p>Класичний стиль для будь-якого випадку</p>
                    </div>
                </div>
            </div>
        </div>

        <div id="modal4" class="modal" onclick="closeModal('modal4')">
            <div class="modal-content" onclick="event.stopPropagation()">
                <span class="close" onclick="closeModal('modal4')">&times;</span>
                <div class="modal-image" style="background: linear-gradient(45deg, #9370db, #da70d6);">
                    <div style="text-align: center;">
                        <h3 style="margin-bottom: 1rem;">💇‍♀️ Омбре</h3>
                        <p>Сучасне градієнтне забарвлення волосся</p>
                    </div>
                </div>
            </div>
        </div>

        <div id="modal5" class="modal" onclick="closeModal('modal5')">
            <div class="modal-content" onclick="event.stopPropagation()">
                <span class="close" onclick="closeModal('modal5')">&times;</span>
                <div class="modal-image" style="background: linear-gradient(45deg, #ff1493, #ffd700);">
                    <div style="text-align: center;">
                        <h3 style="margin-bottom: 1rem;">💄 Денний макіяж</h3>
                        <p>Підкреслення природної краси</p>
                    </div>
                </div>
            </div>
        </div>

        <div id="modal6" class="modal" onclick="closeModal('modal6')">
            <div class="modal-content" onclick="event.stopPropagation()">
                <span class="close" onclick="closeModal('modal6')">&times;</span>
                <div class="modal-image" style="background: linear-gradient(45deg, #4169e1, #ff69b4);">
                    <div style="text-align: center;">
                        <h3 style="margin-bottom: 1rem;">✨ Догляд за обличчям</h3>
                        <p>Професійне очищення та догляд</p>
                    </div>
                </div>
            </div>
        </div>

        <div id="modal7" class="modal" onclick="closeModal('modal7')">
            <div class="modal-content" onclick="event.stopPropagation()">
                <span class="close" onclick="closeModal('modal7')">&times;</span>
                <div class="modal-image" style="background: linear-gradient(45deg, #ff69b4, #9370db);">
                    <div style="text-align: center;">
                        <h3 style="margin-bottom: 1rem;">💇‍♀️ Кучеряве волосся</h3>
                        <p>Об'ємна укладка з природними локонами</p>
                    </div>
                </div>
            </div>
        </div>

        <div id="modal8" class="modal" onclick="closeModal('modal8')">
            <div class="modal-content" onclick="event.stopPropagation()">
                <span class="close" onclick="closeModal('modal8')">&times;</span>
                <div class="modal-image" style="background: linear-gradient(45deg, #ffd700, #ff1493);">
                    <div style="text-align: center;">
                        <h3 style="margin-bottom: 1rem;">💅 Арт-дизайн нігтів</h3>
                        <p>Унікальний дизайн для яскравого образу</p>
                    </div>
                </div>
            </div>
        </div>

        <div id="modal9" class="modal" onclick="closeModal('modal9')">
            <div class="modal-content" onclick="event.stopPropagation()">
                <span class="close" onclick="closeModal('modal9')">&times;</span>
                <div class="modal-image" style="background: linear-gradient(45deg, #da70d6, #4169e1);">
                    <div style="text-align: center;">
                        <h3 style="margin-bottom: 1rem;">💄 Весільний макіяж</h3>
                        <p>Досконалий образ для найважливішого дня</p>
                    </div>
                </div>
            </div>
        </div>

        <footer>
            <div class="container">
                <p>&copy; 2025 {{ get_text('site_title') }}. {{ get_text('footer_text') }}</p>
            </div>
        </footer>

        <script>
            function openModal(modalId) {
                document.getElementById(modalId).style.display = 'block';
                document.body.style.overflow = 'hidden';
            }

            function closeModal(modalId) {
                document.getElementById(modalId).style.display = 'none';
                document.body.style.overflow = 'auto';
            }

            // Close modal with Escape key
            document.addEventListener('keydown', function(event) {
                if (event.key === 'Escape') {
                    const modals = document.querySelectorAll('.modal');
                    modals.forEach(modal => {
                        if (modal.style.display === 'block') {
                            modal.style.display = 'none';
                            document.body.style.overflow = 'auto';
                        }
                    });
                }
            });

            // Smooth scrolling for navigation links
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function (e) {
                    e.preventDefault();
                    const target = document.querySelector(this.getAttribute('href'));
                    if (target) {
                        target.scrollIntoView({
                            behavior: 'smooth',
                            block: 'start'
                        });
                    }
                });
            });
        </script>
    </body>
    </html>
        '''
    return render_template_string(template, get_text=get_text, get_language=get_language)


if __name__ == '__main__':
    app.run(debug=True)