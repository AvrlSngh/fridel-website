function detectSwipe(el, func){
  swipe_det = new Object();
  swipe_det.sX = 0; swipe_det.sY = 0; swipe_det.eX = 0; swipe_det.eY = 0;
  var min_x = 30;
  var max_x = 30;
  var min_y = 50;
  var max_y = 60;
  var direc = "";
  ele = document.getElementById(el);
  ele.addEventListener('touchstart', function(e){
    var t = e.touches[0];
    swipe_det.sX = t.screenX;
    swipe_det.sY = t.screenY;
  }, false);
  ele.addEventListener('touchmove', function(e){
    e.preventDefault();
    var t = e.touches[0];
    swipe_det.eX = t.screenX;
    swipe_det.eY = t.screenY;
  }, false);
  ele.addEventListener('touchend', function(e){
    //horizontal detection
    if ((((swipe_det.eX - min_x > swipe_det.sX) || (swipe_det.eX + min_x < swipe_det.sX)) && ((swipe_det.eY < swipe_det.sY + max_y) && (swipe_det.sY > swipe_det.eY - max_y) && (swipe_det.eX > 0)))) {
      if(swipe_det.eX > swipe_det.sX) direc = "r";
      else direc = "l";
    }

    if (direc != "") {
      if(typeof func == 'function') func(el,direc);
    }
    direc = "";
    swipe_det.sX = 0; swipe_det.sY = 0; swipe_det.eX = 0; swipe_det.eY = 0;
  },false);
}

window.onload = function(){

  var site_nav1 = document.getElementsByClassName('site-nav1')[0];
  var site_nav2 = document.getElementsByClassName('site-nav2')[0];
  var site_nav3 = document.getElementsByClassName('site-nav3')[0];
  var site_nav4 = document.getElementsByClassName('site-nav4')[0];
  var site_nav5 = document.getElementsByClassName('site-nav5')[0];
  var text1 = document.getElementsByClassName('text1')[0];
  var text2 = document.getElementsByClassName('text2')[0];
  var text3 = document.getElementsByClassName('text3')[0];
  var text4 = document.getElementsByClassName('text4')[0];
  var text5 = document.getElementsByClassName('text5')[0];
  var problem_art = document.getElementById('problem_art_img');

  // function animate_text(){
  //   setTimeout(function(){site_nav1.click();}, 1000);
  //   setTimeout(function(){site_nav2.click();}, 10000);
  //   setTimeout(function(){site_nav3.click();}, 20000);
  //   setTimeout(function(){site_nav4.click();}, 30000);
  //   setTimeout(function(){site_nav5.click();}, 40000);
  //   setTimeout(animate_text(), 50000);
  // }; animate_text();

  site_nav1.onclick = function() {
    problem_art.src = "static/problem_art1.png";
    text1.style.display = 'block';
    text2.style.display = 'none';
    text3.style.display = 'none';
    text4.style.display = 'none';
    text5.style.display = 'none';
    site_nav1.style.background = "linear-gradient(to right, #076D37, #90CB24)";
    site_nav2.style.background = "";
    site_nav3.style.background = "";
    site_nav4.style.background = "";
    site_nav5.style.background = "";
  }

  site_nav2.onclick = function() {
    problem_art.src = "static/problem_art2.png";
    text1.style.display = 'none';
    text2.style.display = 'block';
    text3.style.display = 'none';
    text4.style.display = 'none';
    text5.style.display = 'none';
    site_nav1.style.background = "";
    site_nav2.style.background = "linear-gradient(to right, #076D37, #90CB24)";
    site_nav3.style.background = "";
    site_nav4.style.background = "";
    site_nav5.style.background = "";
  }

  site_nav3.onclick = function() {
    problem_art.src = "static/problem_art3.jpg";
    text1.style.display = 'none';
    text2.style.display = 'none';
    text3.style.display = 'block';
    text4.style.display = 'none';
    text5.style.display = 'none';
    site_nav1.style.background = "";
    site_nav2.style.background = "";
    site_nav3.style.background = "linear-gradient(to right, #076D37, #90CB24)";
    site_nav4.style.background = "";
    site_nav5.style.background = "";
  }

  site_nav4.onclick = function() {
    problem_art.src = "static/problem_art4.png";
    text1.style.display = 'none';
    text2.style.display = 'none';
    text3.style.display = 'none';
    text4.style.display = 'block';
    text5.style.display = 'none';
    site_nav1.style.background = "";
    site_nav2.style.background = "";
    site_nav3.style.background = "";
    site_nav4.style.background = "linear-gradient(to right, #076D37, #90CB24)";
    site_nav5.style.background = "";
  }

  site_nav5.onclick = function() {
    problem_art.src = "static/problem_art5.png";
    text1.style.display = 'none';
    text2.style.display = 'none';
    text3.style.display = 'none';
    text4.style.display = 'none';
    text5.style.display = 'block';
    site_nav1.style.background = "";
    site_nav2.style.background = "";
    site_nav3.style.background = "";
    site_nav4.style.background = "";
    site_nav5.style.background = "linear-gradient(to right, #076D37, #90CB24)";
  }
}
