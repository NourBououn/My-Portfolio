document.addEventListener("DOMContentLoaded", function() {
    const projectSearch = document.getElementById("name-search");

    if (!projectSearch) {
        console.log("Search bar not found");
        return; // Exit if the search bar is not found
    }

    const tags = document.querySelectorAll(".tag");
    const projects = document.querySelectorAll(".project");

    function filterProjects() {
        const query = projectSearch.value.toLocaleLowerCase();

        projects.forEach((project) => {
            const name = project.getAttribute('data-name');
            const nameMatch = name.includes(query);

            if (nameMatch) {
                project.style.display = ""; // Show the project
            } else {
                project.style.display = "none"; // Hide the project
            }
        });
    }

    // Add event listeners to filter projects by tags
    tags.forEach((tag) => {
        tag.addEventListener("click", function () {
            const selectedTag = this.getAttribute("data-tag");

            projects.forEach((project) => {
                const projectTags = project.getAttribute("data-tags");
                if (projectTags.includes(selectedTag)) {
                    project.style.display = ""; // Show the project
                } else {
                    project.style.display = "none"; // Hide the project
                }
            });
        });
    });

    // Attach event listener to the search bar for keyup event
    projectSearch.addEventListener("keyup", filterProjects);
});