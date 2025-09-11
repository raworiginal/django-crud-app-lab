const addTrackBtn = document.querySelector("#track-add-btn");
const addTrackForm = document.querySelector("#track-add-form");

addTrackBtn.addEventListener("click", () => {
	addTrackForm.showModal();
});
