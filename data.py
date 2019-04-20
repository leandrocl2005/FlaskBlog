import datetime

categorias = [
    {
        "id": 1,
        "name": "Front-End",
        "slug": "frontend",
        "css_class": "cat-1"
    },
    {
        "id": 2,
        "name": "Back-End",
        "slug": "backend",
        "css_class": "cat-2"
    },
    {
        "id": 3,
        "name": "DB",
        "slug": "db",
        "css_class": "cat-3"
    },
    {
        "id": 4,
        "name": "AI",
        "slug": "ai",
        "css_class": "cat-4"
    }
]

users = [
    {
        "id": 1,
        "username": "yota",
        "bio": "Uhu, nóis não sabe nem falar o português.",
        "email": 'yotabigdata@gmail.com',
        "pic": 'https://lh3.googleusercontent.com/-vsms9NSE6jc/'
        'AAAAAAAAAAI/AAAAAAAAAAc/Ulw49DA12UQ/photo.jpg',
        "social_id": '114180459126034289074',
    },
    {
        "id": 2,
        "username": "Leandro",
        "bio": "Um cara legal tentando aprender Flask, mas tá osso.",
        "email": 'leandrocl2006@gmail.com',
        "pic": 'https://lh6.googleusercontent.com/-vkI83QN-EOQ/'
        'AAAAAAAAAAI/AAAAAAAAADs/B0w34yhElIA/photo.jpg',
        "social_id": '110036420567886642461',
    }
]

posts = [
    {
        "id": 1,
        "categoria_id": 1,
        "user_id": 2,
        "publish_date": datetime.datetime(2017, 2, 13),
        "title": "Aprendendo CSS",
        "body": """
        <p>Mussum Ipsum, cacilds vidis litro abertis. Per
        aumento de cachacis, eu reclamis. Mauris nec dolor
        in eros commodo tempor. Aenean aliquam molestie leo,
        vitae iaculis nisl. Nec orci ornare consequat.
        Praesent lacinia ultrices consectetur.
        Sed non ipsum felis. Em pé sem cair, deitado sem dormir,
        sentado sem cochilar e fazendo pose.</p>
        <p>Diuretics paradis num copo é motivis de denguis.
        A ordem dos tratores não altera o pão duris.
        Atirei o pau no gatis, per gatis num morreus.
        Detraxit consequat et quo num tendi nada.</p>
        <p>Tá deprimidis, eu conheço uma cachacis que
        pode alegrar sua vidis. Nullam volutpat risus
        nec leo commodo, ut interdum diam laoreet.
        Sed non consequat odio. Interessantiss quisso
        pudia ce receita de bolis, mais bolis eu num gostis.
        Praesent malesuada urna nisi, quis volutpat erat
        hendrerit non. Nam vulputate dapibus.</p>
        """,
        "pic": "img/post-1.jpg",
        "abstract": "Aprenda de maneira simples, prática e rápido!",
        "featured": True,
        "start_page": False
    },
    {
        "id": 2,
        "categoria_id": 2,
        "user_id": 1,
        "publish_date": datetime.datetime(2018, 12, 15),
        "title": "Aprendendo Python",
        "body": """
        <p>Mussum Ipsum, cacilds vidis litro abertis. Per
        aumento de cachacis, eu reclamis. Mauris nec dolor
        in eros commodo tempor. Aenean aliquam molestie leo,
        vitae iaculis nisl. Nec orci ornare consequat.
        Praesent lacinia ultrices consectetur.
        Sed non ipsum felis. Em pé sem cair, deitado sem dormir,
        sentado sem cochilar e fazendo pose.</p>
        <p>Diuretics paradis num copo é motivis de denguis.
        A ordem dos tratores não altera o pão duris.
        Atirei o pau no gatis, per gatis num morreus.
        Detraxit consequat et quo num tendi nada.</p>
        <p>Tá deprimidis, eu conheço uma cachacis que
        pode alegrar sua vidis. Nullam volutpat risus
        nec leo commodo, ut interdum diam laoreet.
        Sed non consequat odio. Interessantiss quisso
        pudia ce receita de bolis, mais bolis eu num gostis.
        Praesent malesuada urna nisi, quis volutpat erat
        hendrerit non. Nam vulputate dapibus.</p>
        """,
        "pic": "img/post-2.jpg",
        "abstract": "Você sabe o que é um Dragão brasileiro?",
        "featured": True,
        "start_page": False
    },
    {
        "id": 3,
        "categoria_id": 4,
        "user_id": 2,
        "publish_date": datetime.datetime(2019, 1, 13),
        "title": "Tunando Florestas",
        "body": """
        <p>Mussum Ipsum, cacilds vidis litro abertis. Per
        aumento de cachacis, eu reclamis. Mauris nec dolor
        in eros commodo tempor. Aenean aliquam molestie leo,
        vitae iaculis nisl. Nec orci ornare consequat.
        Praesent lacinia ultrices consectetur.
        Sed non ipsum felis. Em pé sem cair, deitado sem dormir,
        sentado sem cochilar e fazendo pose.</p>
        <p>Diuretics paradis num copo é motivis de denguis.
        A ordem dos tratores não altera o pão duris.
        Atirei o pau no gatis, per gatis num morreus.
        Detraxit consequat et quo num tendi nada.</p>
        <p>Tá deprimidis, eu conheço uma cachacis que
        pode alegrar sua vidis. Nullam volutpat risus
        nec leo commodo, ut interdum diam laoreet.
        Sed non consequat odio. Interessantiss quisso
        pudia ce receita de bolis, mais bolis eu num gostis.
        Praesent malesuada urna nisi, quis volutpat erat
        hendrerit non. Nam vulputate dapibus.</p>
        """,
        "pic": "img/post-3.jpg",
        "abstract": "E se o Random Forest fosse ainda melhor?",
        "featured": False,
        "start_page": False
    },
    {
        "id": 4,
        "categoria_id": 3,
        "user_id": 1,
        "publish_date": datetime.datetime(2018, 8, 15),
        "title": "O futuro dos NoSQL's",
        "body": """
        <p>Mussum Ipsum, cacilds vidis litro abertis. Per
        aumento de cachacis, eu reclamis. Mauris nec dolor
        in eros commodo tempor. Aenean aliquam molestie leo,
        vitae iaculis nisl. Nec orci ornare consequat.
        Praesent lacinia ultrices consectetur.
        Sed non ipsum felis. Em pé sem cair, deitado sem dormir,
        sentado sem cochilar e fazendo pose.</p>
        <p>Diuretics paradis num copo é motivis de denguis.
        A ordem dos tratores não altera o pão duris.
        Atirei o pau no gatis, per gatis num morreus.
        Detraxit consequat et quo num tendi nada.</p>
        <p>Tá deprimidis, eu conheço uma cachacis que
        pode alegrar sua vidis. Nullam volutpat risus
        nec leo commodo, ut interdum diam laoreet.
        Sed non consequat odio. Interessantiss quisso
        pudia ce receita de bolis, mais bolis eu num gostis.
        Praesent malesuada urna nisi, quis volutpat erat
        hendrerit non. Nam vulputate dapibus.</p>
        """,
        "pic": "img/post-4.jpg",
        "abstract": "Conheça a terra sem lei dos DB's",
        "featured": True,
        "start_page": True
    },
    {
        "id": 5,
        "categoria_id": 1,
        "user_id": 1,
        "publish_date": datetime.datetime(2018, 9, 15),
        "title": "A eterna briga com as janelas",
        "body": """
        <p>Mussum Ipsum, cacilds vidis litro abertis. Per
        aumento de cachacis, eu reclamis. Mauris nec dolor
        in eros commodo tempor. Aenean aliquam molestie leo,
        vitae iaculis nisl. Nec orci ornare consequat.
        Praesent lacinia ultrices consectetur.
        Sed non ipsum felis. Em pé sem cair, deitado sem dormir,
        sentado sem cochilar e fazendo pose.</p>
        <p>Diuretics paradis num copo é motivis de denguis.
        A ordem dos tratores não altera o pão duris.
        Atirei o pau no gatis, per gatis num morreus.
        Detraxit consequat et quo num tendi nada.</p>
        <p>Tá deprimidis, eu conheço uma cachacis que
        pode alegrar sua vidis. Nullam volutpat risus
        nec leo commodo, ut interdum diam laoreet.
        Sed non consequat odio. Interessantiss quisso
        pudia ce receita de bolis, mais bolis eu num gostis.
        Praesent malesuada urna nisi, quis volutpat erat
        hendrerit non. Nam vulputate dapibus.</p>
        """,
        "pic": "img/post-5.jpg",
        "abstract": "Resolva seus problema com grides!",
        "featured": False,
        "start_page": True
    },
    {
        "id": 6,
        "categoria_id": 3,
        "user_id": 1,
        "publish_date": datetime.datetime(2018, 10, 15),
        "title": "SQL ou NoSQL?",
        "body": """
        <p>Mussum Ipsum, cacilds vidis litro abertis. Per
        aumento de cachacis, eu reclamis. Mauris nec dolor
        in eros commodo tempor. Aenean aliquam molestie leo,
        vitae iaculis nisl. Nec orci ornare consequat.
        Praesent lacinia ultrices consectetur.
        Sed non ipsum felis. Em pé sem cair, deitado sem dormir,
        sentado sem cochilar e fazendo pose.</p>
        <p>Diuretics paradis num copo é motivis de denguis.
        A ordem dos tratores não altera o pão duris.
        Atirei o pau no gatis, per gatis num morreus.
        Detraxit consequat et quo num tendi nada.</p>
        <p>Tá deprimidis, eu conheço uma cachacis que
        pode alegrar sua vidis. Nullam volutpat risus
        nec leo commodo, ut interdum diam laoreet.
        Sed non consequat odio. Interessantiss quisso
        pudia ce receita de bolis, mais bolis eu num gostis.
        Praesent malesuada urna nisi, quis volutpat erat
        hendrerit non. Nam vulputate dapibus.</p>
        """,
        "pic": "img/post-6.jpg",
        "abstract": "Qual estrutura de banco de dadis é melhor?",
        "featured": True,
        "start_page": False
    },
    {
        "id": 7,
        "categoria_id": 4,
        "user_id": 2,
        "publish_date": datetime.datetime(2019, 3, 15),
        "title": "Faça seu computador reconhecer seu cachorro",
        "body": """
        <p>Mussum Ipsum, cacilds vidis litro abertis. Per
        aumento de cachacis, eu reclamis. Mauris nec dolor
        in eros commodo tempor. Aenean aliquam molestie leo,
        vitae iaculis nisl. Nec orci ornare consequat.
        Praesent lacinia ultrices consectetur.
        Sed non ipsum felis. Em pé sem cair, deitado sem dormir,
        sentado sem cochilar e fazendo pose.</p>
        <p>Diuretics paradis num copo é motivis de denguis.
        A ordem dos tratores não altera o pão duris.
        Atirei o pau no gatis, per gatis num morreus.
        Detraxit consequat et quo num tendi nada.</p>
        <p>Tá deprimidis, eu conheço uma cachacis que
        pode alegrar sua vidis. Nullam volutpat risus
        nec leo commodo, ut interdum diam laoreet.
        Sed non consequat odio. Interessantiss quisso
        pudia ce receita de bolis, mais bolis eu num gostis.
        Praesent malesuada urna nisi, quis volutpat erat
        hendrerit non. Nam vulputate dapibus.</p>
        """,
        "pic": "img/post-7.jpg",
        "abstract": "Conheça ANN's, as famosas redes neurais artificiais",
        "featured": True,
        "start_page": False
    },
    {
        "id": 8,
        "categoria_id": 2,
        "user_id": 1,
        "publish_date": datetime.datetime(2019, 4, 15),
        "title": "Matemática para programadores",
        "body": """
        <p>Mussum Ipsum, cacilds vidis litro abertis. Per
        aumento de cachacis, eu reclamis. Mauris nec dolor
        in eros commodo tempor. Aenean aliquam molestie leo,
        vitae iaculis nisl. Nec orci ornare consequat.
        Praesent lacinia ultrices consectetur.
        Sed non ipsum felis. Em pé sem cair, deitado sem dormir,
        sentado sem cochilar e fazendo pose.</p>
        <p>Diuretics paradis num copo é motivis de denguis.
        A ordem dos tratores não altera o pão duris.
        Atirei o pau no gatis, per gatis num morreus.
        Detraxit consequat et quo num tendi nada.</p>
        <p>Tá deprimidis, eu conheço uma cachacis que
        pode alegrar sua vidis. Nullam volutpat risus
        nec leo commodo, ut interdum diam laoreet.
        Sed non consequat odio. Interessantiss quisso
        pudia ce receita de bolis, mais bolis eu num gostis.
        Praesent malesuada urna nisi, quis volutpat erat
        hendrerit non. Nam vulputate dapibus.</p>
        """,
        "pic": "img/post-8.jpg",
        "abstract": "Você pode ter aplicações mais rápidas com ela",
        "featured": False,
        "start_page": False
    },
    {
        "id": 9,
        "categoria_id": 2,
        "user_id": 1,
        "publish_date": datetime.datetime(2019, 5, 15),
        "title": "REGEX, a linguagem secreta dos programadores",
        "body": """
        <p>Mussum Ipsum, cacilds vidis litro abertis. Per
        aumento de cachacis, eu reclamis. Mauris nec dolor
        in eros commodo tempor. Aenean aliquam molestie leo,
        vitae iaculis nisl. Nec orci ornare consequat.
        Praesent lacinia ultrices consectetur.
        Sed non ipsum felis. Em pé sem cair, deitado sem dormir,
        sentado sem cochilar e fazendo pose.</p>
        <p>Diuretics paradis num copo é motivis de denguis.
        A ordem dos tratores não altera o pão duris.
        Atirei o pau no gatis, per gatis num morreus.
        Detraxit consequat et quo num tendi nada.</p>
        <p>Tá deprimidis, eu conheço uma cachacis que
        pode alegrar sua vidis. Nullam volutpat risus
        nec leo commodo, ut interdum diam laoreet.
        Sed non consequat odio. Interessantiss quisso
        pudia ce receita de bolis, mais bolis eu num gostis.
        Praesent malesuada urna nisi, quis volutpat erat
        hendrerit non. Nam vulputate dapibus.</p>
        """,
        "pic": "img/post-9.jpg",
        "abstract": "Você fala REGEX?",
        "featured": True,
        "start_page": False
    },
]
