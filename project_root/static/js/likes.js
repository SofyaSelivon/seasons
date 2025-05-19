function initLikeSystem() {
    const socket = new WebSocket('ws://127.0.0.1:8000/ws/likes/index/');

    const likeBtn = document.getElementById('like-btn');
    const dislikeBtn = document.getElementById('dislike-btn');
    const likeCount = document.getElementById('like-count');
    const dislikeCount = document.getElementById('dislike-count');

    socket.onmessage = (e) => {
        const data = JSON.parse(e.data);
        if (data.type === 'counts') {
            likeCount.textContent = data.likes;
            dislikeCount.textContent = data.dislikes;
        }
        if (data.type === 'error') {
            alert(data.message);
        }
    };

    likeBtn.addEventListener('click', () => {
        socket.send(JSON.stringify({ action: 'like' }));
    });

    dislikeBtn.addEventListener('click', () => {
        socket.send(JSON.stringify({ action: 'dislike' }));
    });

    socket.onerror = (e) => {
        console.error('WebSocket error:', e);
    };

    setInterval(() => {
        socket.send(JSON.stringify({ action: 'ping' }));
    }, 1000);
}

document.addEventListener('DOMContentLoaded', initLikeSystem);
