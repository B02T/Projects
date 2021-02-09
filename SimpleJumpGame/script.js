document.addEventListener("DOMContentLoaded", () => {
  const prince = document.querySelector(".character");
  let bottom = 0;
  let gravity = 0.9;
  let isJumping = false;

  function jump() {
    if (isJumping) return;
    timerId = setInterval(function () {
      if (bottom > 250) {
        clearInterval(timerId);
        let timerDownId = setInterval(function () {
          bottom -= 5;
          prince.style.bottom = bottom + "px";
          if (bottom < 0) {
            clearInterval(timerDownId);
            isJumping = false;
          }
        }, 20);
      }
      isJumping = true;
      bottom += 30;
      prince.style.bottom = bottom * gravity + "px";
      console.log(bottom * gravity);
    }, 20);
  }

  function control(e) {
    if (e.keyCode === 38) {
      jump();
    }
  }

  document.addEventListener("keydown", control);

  //end
});
