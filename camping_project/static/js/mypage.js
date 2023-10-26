if (window.location.pathname === "/user/mypage/1") {
    setTimeout(initPage, 1000);
}

function initPage() {
    const editButton = document.getElementById("edit_button");
    const cancelButton = document.getElementById("cancel_button");
    const editProfileBlock = document.getElementById("edit_profile_block");
    const userInfoUpdate = document.getElementById("user_info_update");

    if (editButton && cancelButton && editProfileBlock && userInfoUpdate) {
        editButton.addEventListener("click", function() {
            editProfileBlock.style.display = "block";
            userInfoUpdate.style.display = "none";
            cancelButton.style.display = "block";
            editButton.style.display = "none";
        });

        cancelButton.addEventListener("click", function() {
            editProfileBlock.style.display = "none";
            userInfoUpdate.style.display = "block";
            cancelButton.style.display = "none";
            editButton.style.display = "block";
        });
    } else {
        console.error("One or more elements not found.");
    }
}