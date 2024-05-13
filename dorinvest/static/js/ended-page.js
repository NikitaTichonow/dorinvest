document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.ended-page__show').forEach(function (showBlock) {
        showBlock.addEventListener('click', function () {
            let description = showBlock.parentNode.querySelector('.ended-page__show__description');
            if (description.style.height) {
                description.style.height = null;
            } else {
                const height = (description.scrollHeight + 50) + "px";
                description.style.height = height;
            }
            description.classList.toggle('active');
            showBlock.classList.toggle('active');

            let rotateButton = showBlock.querySelector('.ended-page__rotate-button img');
            rotateButton.classList.toggle('rotated');
        });
    });
});