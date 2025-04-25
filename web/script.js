function sendMessage() {
    const input = document.getElementById('user-input').value;
    if (input.trim() !== '') {
        const chatWindow = document.getElementById('chat-window');
        const userMessage = document.createElement('div');
        userMessage.textContent = 'Вы: ' + input;
        chatWindow.appendChild(userMessage);
        document.getElementById('user-input').value = '';
        // Здесь будет отправка запроса на сервер
    }
}
