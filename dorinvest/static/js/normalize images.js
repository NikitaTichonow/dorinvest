// приводим высоту всех изображений к одному значению (среднестатистическому)

let images = document.querySelector('.image-slider__wraper').querySelectorAll('img')

function getMidImgHeight() {
    let sizesSum = 0;

    for (let img of images) {
        sizesSum += img.naturalHeight
    };

    return sizesSum / images.length;
};

function normilizeImgs() {
    let midImgHeight = getMidImgHeight();
    let maxHeight = document.body.clientHeight * 0.60

    let height = Math.min(midImgHeight, maxHeight)

    for (let img of images) {
        img.style['max-height'] = height + 'px';
        img.style.width = 'auto';
    };
};


normilizeImgs();