window.addEventListener('DOMContentLoaded', () => {
    let scrollPos = 0;
    const nav = document.getElementById('nav');
    window.addEventListener('scroll', function() {
        const currentTop = document.body.getBoundingClientRect().top * -1;
        if ( currentTop < scrollPos) {
            // Scrolling Up
            if (currentTop > 0 && nav.classList.contains('is-fixed')) {
                nav.classList.add('is-visible');
            } else {
                console.log(123);
                nav.classList.remove('is-visible', 'is-fixed');
            }
        } else {
            // Scrolling Down
            nav.classList.remove(['is-visible']);
            if (currentTop > nav.clientHeight && !nav.classList.contains('is-fixed')) {
                nav.classList.add('is-fixed');
            }
        }
        scrollPos = currentTop;
    });
})