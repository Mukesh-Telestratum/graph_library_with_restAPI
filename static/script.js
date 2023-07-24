function showNodeInputs() {
    // Get the number of nodes from the input field
    var numNodes = document.getElementById("num_nodes").value;
    var nodeFields = document.getElementById("nodeFields");
    nodeFields.innerHTML = "";
  
    // Create input fields for each node
    for (var i = 0; i < numNodes; i++) {
      var label = document.createElement("label");
      label.textContent = "Node " + (i + 1) + ":";
  
      var input = document.createElement("input");
      input.setAttribute("type", "text");
      input.setAttribute("name", "node_" + i);
      input.setAttribute("required", "");
  
      var br = document.createElement("br");
      nodeFields.appendChild(label);
      nodeFields.appendChild(input);
      nodeFields.appendChild(br);
    }
  
    // Show the node input section and the submit button
    document.getElementById("nodeInputs").classList.remove("hidden");
    document.getElementById("nodeSubmitBtn").classList.remove("hidden");
  }
  
  function showEdgeCountInput() {
    // Show the edge count input section and the submit button
    document.getElementById("edgeCountInput").classList.remove("hidden");
    document.getElementById("edgeCountSubmitBtn").classList.remove("hidden");
  }
  
  function showEdgeInputs() {
    // Get the number of edges from the input field
    var numEdges = document.getElementById("num_edges").value;
    var edgeFields = document.getElementById("edgeFields");
    edgeFields.innerHTML = "";
  
    // Create input fields for each edge
    for (var i = 0; i < numEdges; i++) {
      var fromLabel = document.createElement("label");
      fromLabel.textContent = "From Node:";
  
      var fromInput = document.createElement("input");
      fromInput.setAttribute("type", "text");
      fromInput.setAttribute("name", "from_node_" + i);
      fromInput.setAttribute("required", "");
  
      var toLabel = document.createElement("label");
      toLabel.textContent = "To Node:";
  
      var toInput = document.createElement("input");
      toInput.setAttribute("type", "text");
      toInput.setAttribute("name", "to_node_" + i);
      toInput.setAttribute("required", "");
  
      var weight1Label = document.createElement("label");
      weight1Label.textContent = "Forward:";
  
      var weight1Input = document.createElement("input");
      weight1Input.setAttribute("type", "number");
      weight1Input.setAttribute("name", "weight1_" + i);
      weight1Input.setAttribute("required", "");
  
      var useWeight2Label = document.createElement("label"); // Label for backward weight checkbox
      useWeight2Label.textContent = "Add Backward:";
  
      var useWeight2Input = document.createElement("input"); // Checkbox for backward weight
      useWeight2Input.setAttribute("type", "checkbox");
      useWeight2Input.setAttribute("name", "use_weight2_" + i);
      useWeight2Input.addEventListener("change", function () {
        toggleBackwardInput(this);
      });
  
      var weight2Label = document.createElement("label");
      weight2Label.textContent = "Backward:";
      weight2Label.style.display = "none";
  
      var weight2Input = document.createElement("input");
      weight2Input.setAttribute("type", "number");
      weight2Input.setAttribute("name", "weight2_" + i);
      weight2Input.style.display = "none";
  
      // Append the elements to the edgeFields container
      edgeFields.appendChild(fromLabel);
      edgeFields.appendChild(fromInput);
      edgeFields.appendChild(toLabel);
      edgeFields.appendChild(toInput);
      edgeFields.appendChild(weight1Label);
      edgeFields.appendChild(weight1Input);
      edgeFields.appendChild(useWeight2Label);
      edgeFields.appendChild(useWeight2Input);
      edgeFields.appendChild(weight2Label);
      edgeFields.appendChild(weight2Input);
      edgeFields.appendChild(document.createElement("br"));
    }
  
    // Show the edge input section and the create graph button
    document.getElementById("edgeInputs").classList.remove("hidden");
    document.getElementById("createGraphBtn").classList.remove("hidden");
  }
  
  function toggleBackwardInput(checkbox) {
    // Toggle the visibility of the backward weight input based on the checkbox state
    var weight2Label = checkbox.nextElementSibling.nextElementSibling;
    var weight2Input = weight2Label.nextElementSibling;
  
    if (checkbox.checked) {
      weight2Label.style.display = "inline";
      weight2Input.style.display = "inline";
    } else {
      weight2Label.style.display = "none";
      weight2Input.style.display = "none";
    }
  }