// 요일별 스와이퍼 메소드
function swiperInitialize() {
  var d = new Date();
  var n = d.getDay();
  if (screen >= 1000) {
    swiper.initialSlide = n - 1;
  } else {
    swiper.initialSlide = n;
  }
}

// 네비게이션바 호출 함수
// $.get("/static/navigation.html", function (data) {
//   $("#nav-placeholder").replaceWith(data);
// });
