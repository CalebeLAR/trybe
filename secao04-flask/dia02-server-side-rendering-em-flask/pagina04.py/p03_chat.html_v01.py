# noqa: E501

# <!-- Section é uma tag html para criar um componente -->
# <section class="messenger">
#   <!-- cabeçalho -->
#   <header class="messenger-header">
#     <meta charset="UTF-8">
#     <title>Chat Trybot</title>

#     <!-- Carrega o CSS estático -->
#     <link rel="stylesheet" href="{{ url_for('static', filename='css/chat.css') }}">

#     <div class="messenger-header-title">
#       <i class="fas fa-comment-alt"> Trybot</i>
#     </div>

#     <div class="messenger-header-options">
#       <span><i class="fas fa-cog"></i></span>
#     </div>
#   </header>

#   <main class="messenger-chat" id="chat">
#     <!-- loop for nas mensagens recebidas da controller -->
#     {% for message in session_messages %}
#       <!-- se mensagem é do Trybot, deve alinhar a esquerda e definir avatar-->
#       {% if message['from'] == 'Trybot' %}
#         {% set class_message = 'left-msg' %}
#         {% set file_name = 'images/avatar.png' %}
#       {% else %}
#         {% set class_message = 'right-msg' %}
#         {% set file_name = 'images/avatar-user.png' %}
#       {% endif %}

#       <div class="msg {{ class_message }}">
#         <div class="msg-avatar">
#           <img src="{{ url_for('static', filename=file_name)}}" width="100%">
#         </div>

#         <div class="msg-ballon">
#           <div class="msg-info">
#             <div class="msg-info-name">{{ message['from'] }}</div>
#             <div class="msg-info-time">{{ message['time'] }}</div>
#           </div>

#           <div class="msg-text">
#             {{message['content']|safe}}
#           </div>
#         </div>
#       </div>
#     {% endfor %}
#   </main>

#   <form method="post" class="messenger-inputarea">
#     <input type="text" name="message-content" class="messenger-input" placeholder="Escreva sua mensagem...">
#     <input type="hidden" name="username" value="{{ username }}">
#     <button type="submit" class="messenger-send-btn">Enviar</button>
#   </form>
# </section>

# <!-- Não somos contra Javascript! Podemos usar também 😄 -->
# <!-- Aqui, ele serve para descer a barra de rolagem ao carregar o chat-->
# <script>
#   if (window.history.replaceState) {
#     window.history.replaceState(null, null, window.location.href);
#   }
#   var chatDiv = document.getElementById("chat");
#   chatDiv.scrollTop = chatDiv.scrollHeight;
# </script>
