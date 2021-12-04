$(document).ready(function () {
        function check_theme() {
            if (localStorage.getItem("theme") === "dark") {
                $(".logo").attr('src', "static/images/Shooble-logos/Shooble-logos_white.png")
                $("body").addClass("dark");
                $(".card").addClass("dark-card-feed");
                $(".content-card").addClass("dark-card");
                $(".like-button-text").addClass("text-white")
                $(".change").text("ON");
            } else if (localStorage.getItem("theme") === "light") {
                $(".logo").attr('src', "static/images/Shooble-logos/Shooble-logos_black.png")
                $("body").removeClass("dark");
                $(".card").removeClass("dark-card-feed");
                $(".content-card").removeClass("dark-card");
                $(".like-button-text").removeClass("text-white")
                $(".change").text("OFF");
            }
        }

        $(".dark-mode-switch").on("click", function () {
            if ($("body").hasClass("dark")) {
                console.log("Switched to light mode")
                localStorage.setItem("theme", "light");
                check_theme()
            } else {
                console.log("Switched to dark mode")
                localStorage.setItem("theme", "dark");
                check_theme()
            }
        });
        check_theme()
    });