// Sample data: Array of grades
const grades = [85, 90, 78, 92, 88, 76, 95];

// Function to calculate the average
function calculateAverage(grades) {
    const sum = grades.reduce((acc, grade) => acc + grade, 0);
    return (sum / grades.length).toFixed(2); // Format to 2 decimal places
}

// Display the average on page load
document.addEventListener("DOMContentLoaded", () => {
    const averageDisplay = document.getElementById("average-display");
    const classAverage = calculateAverage(grades);
    averageDisplay.textContent = `Current Class Average: ${classAverage}`;
});

function drawGauge(classAverage, passMark) {
    const maxDegree = 180; // 0 to 180 degrees for half-circle gauge
    const maxScore = 100;  // Assuming max score is 100
    const rotation = (classAverage / maxScore) * maxDegree;
  
    const needle = document.createElement('div');
    needle.classList.add('needle');
    needle.style.transform = `rotate(${rotation}deg)`;
  
    const gaugeContainer = document.getElementById('gauge-container');
    gaugeContainer.innerHTML = ''; // Clear previous needle if needed
    gaugeContainer.appendChild(needle);
  
    // Add a visual indicator for the pass threshold
    if (passMark) {
      const passMarkRotation = (passMark / maxScore) * maxDegree;
      const passMarker = document.createElement('div');
      passMarker.classList.add('needle');
      passMarker.style.background = 'green';
      passMarker.style.transform = `rotate(${passMarkRotation}deg)`;
      passMarker.style.height = '10px';
      gaugeContainer.appendChild(passMarker);
    }
  }
  
  // Example call with 75 as class average and 50 as pass mark
  drawGauge(75, 50);
  
