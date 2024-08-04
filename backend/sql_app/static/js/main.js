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
https: $.get("navigation.html", function (data) {
  $("#nav-placeholder").replaceWith(data);
});

// 요일별 분리수거 업데이트 -- API 생성 후 다시 확인!!!
async function updateSchedule() {
  const region = document.getElementById("gugun").value;
  if (!region) return;

  try {
    const schedule = await fetchSchedule(region);
    populateSwiper(schedule);
  } catch (error) {
    console.error("Error fetching schedule:", error);
  }
}

document.getElementById("gugun").addEventListener("change", updateSchedule);

//대형 폐기물 탭메뉴 선택 JS
document.addEventListener("DOMContentLoaded", function () {
  const tabs = document.querySelectorAll(".tab-item");
  const tabPanes = document.querySelectorAll(".tab-pane");

  tabs.forEach((tab) => {
    tab.addEventListener("click", function (e) {
      e.preventDefault();
      const target = tab.getAttribute("data-tab");

      // Remove active class from all tabs
      tabs.forEach((t) => t.classList.remove("active"));
      // Remove active class from all tab panes
      tabPanes.forEach((pane) => pane.classList.remove("active"));

      // Add active class to clicked tab
      tab.classList.add("active");
      // Add active class to corresponding tab pane
      document.getElementById(target).classList.add("active");
    });
  });
});
