'use strict'
//vscode knows that we return canvas
//  /** @type {WebGLRenderingContext} */
 /** @type {HTMLCanvasElement} */

const canvas = document.getElementById('canvas1');
const ctx = canvas.getContext('2d');
canvas.width = innerWidth;
canvas.height = innerHeight;

window.addEventListener('resize', function(){
    canvas.width = innerWidth;
    canvas.height = innerHeight;
});

const mouse = {
    x:undefined,
    y:undefined
};

function randomNumber(){
    return Math.floor(Math.random * 100);
}

function randomColor(){
    const arr = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += arr[Math.floor(Math.random() * 16)];    
    }
    return color;
}

function createCitcle(){
    ctx.fillStyle=randomColor();
    ctx.beginPath();
    ctx.arc(mouse.x,mouse.y,10,0,Math.PI * 2);
    ctx.fill();
}

canvas.addEventListener('mousemove', function(e){
    mouse.x = e.x;
    mouse.y = e.y;
    createCitcle();
});

