$(document).ready(function() {
    // Obtener el ID de conversación
    var conversationId = $('#conversation-id').val();

    // Función para mostrar los mensajes
    function displayMessages(messages) {
        var messageList = $('#message-list');
        messageList.empty();

        messages.forEach(function(message) {
            var listItem = $('<li>').text(message.sender + ': ' + message.content + ' (' + message.timestamp + ')');
            messageList.append(listItem);
        });
    }

    // Obtener y mostrar mensajes anteriores
    $.ajax({
        url: '/get-messages/',
        method: 'GET',
        data: {
            conversation_id: conversationId
        },
        success: function(response) {
            displayMessages(response.messages);
        }
    });

    // Enviar un nuevo mensaje
    $('#send-button').on('click', function() {
        var message = $('#message-input').val();

        $.ajax({
            url: '/send-message/',
            method: 'POST',
            data: {
                conversation_id: conversationId,
                message: message,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(response) {
                if (response.status === 'success') {
                    // Actualizar la lista de mensajes
                    displayMessages(response.messages);

                    // Limpiar el campo de entrada de mensaje
                    $('#message-input').val('');
                } else {
                    console.log('Error al enviar el mensaje');
                }
            }
        });
    });
});
