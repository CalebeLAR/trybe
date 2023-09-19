"""
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title>Chat Trybot</title>
    <!-- {{url_for}} utilizado para importar um css estático -->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
</head>

<body class="container">
    <!-- {{url_for}} utilizado para importar uma imagem estática -->
    <img src="{{ url_for('static', filename='images/logo.png') }}" width="40%">

    <form action="/" method="post">
        <p>Olá! Bom dia, como você se chama?</p>
        <div class="send-box">
            <input type="text" name="username">
            <button type="submit" id="chat">Entrar</button>
        </div>
    </form>
</body>
</html>
"""
