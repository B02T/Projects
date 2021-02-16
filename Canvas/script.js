'use strict'
//vscode knows that we return canvas
//  /** @type {WebGLRenderingContext} */
 /** @type {HTMLCanvasElement} */


const canvas = document.getElementById('canvas1');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    a.build()
});

class Rect{
    constructor(){
        this.posx = 0;
        this.posy = 0;
        this.width = 100;
        this.height = 100;
    }

    build(){
        ctx.fillStyle = "red";
        ctx.fillRect(this.posx, this.posy, this.width, this.height);
    }
}

const a = new Rect();
a.build()
console.log(a);