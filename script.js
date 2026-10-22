const button = document.getElementById("run-button");
const output = document.getElementById("output");
const status = document.getElementById("status");

button.addEventListener("click", async () => {
  button.disabled = true;
  status.textContent = "Running Python program…";
  output.textContent = "";

  try {
    const response = await fetch("/api/run", {method: "POST"});
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || "The program could not run.");
    output.textContent = data.output || "(The program did not print any output.)";
    status.textContent = "Finished.";
  } catch (error) {
    status.textContent = "Something went wrong.";
    output.textContent = error.message;
  } finally {
    button.disabled = false;
  }
});
