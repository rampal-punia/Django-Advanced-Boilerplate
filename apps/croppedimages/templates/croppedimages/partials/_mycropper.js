$(document).ready(function () {
    const image = document.getElementById('image');
    let eventDetailX
    let eventDetailY
    let eventDetailWidth
    let eventDetailHeigth
    const cropper = new Cropper(image, {
        // aspectRatio: 1 / 1,
        crop(event) {
            eventDetailX = event.detail.x
            eventDetailY = event.detail.y
            eventDetailWidth = event.detail.width
            eventDetailHeigth = event.detail.height
            // console.log(event.detail.rotate);
            // console.log(event.detail.scaleX);
            // console.log(event.detail.scaleY);
        },
    })
    $("#saveCroppedAreaBtn").click(function (e) {
        e.preventDefault();
        let csrf = $("input[name=csrfmiddlewaretoken]").val()
        let imageId = JSON.parse(document.getElementById("imageId").textContent)
        let crop = true
        let expData = {
            csrfmiddlewaretoken: csrf,
            x: eventDetailX,
            y: eventDetailY,
            w: eventDetailWidth,
            h: eventDetailHeigth,
            imageId: imageId,
            crop: crop,
        }
        $.ajax({
            type: "post",
            url: "{% url 'croppedimages:crop_image_js_url' %}",
            data: expData,
            // dataType: "dataType",
            success: function (response) {
                $("#croppedImageDiv").html(`<img src="${response["img_url"]}" id="croppedImage">`);
                cropped_img_id = response["cropped_img_id"]
                cropped_img_url = response["cropped_img_url"]
            }
        });
    })
});
// const image = document.getElementById('image');
// const cropper = new Cropper(image, {
//   aspectRatio: 16 / 9,
//   crop(event) {
//     console.log(event.detail.x);
//     console.log(event.detail.y);
//     console.log(event.detail.width);
//     console.log(event.detail.height);
//     console.log(event.detail.rotate);
//     console.log(event.detail.scaleX);
//     console.log(event.detail.scaleY);
//   },
// });

