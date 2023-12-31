var canvas, ctx;
function startGame() {
    canvas = document.getElementById("gameCanvas");
    ctx = canvas.getContext("2d");
    ctx.fillStyle = "#FF0000";
    ctx.fillRect(20, 20, 50, 50);
}
