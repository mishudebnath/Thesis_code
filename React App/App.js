import React, { useState } from "react";
import "./App.css"; // Importing CSS

const initialData = [
  {
    timestamp: "08/07/2020 12:02",
    gender: "Female",
    age: 18,
    course: "CSE",
    year: "Year 1",
    cgpa: "3.00 - 3.49",
    maritalStatus: "No",
    depression: "Yes",
    anxiety: "Yes",
    panicAttack: "Yes",
    treatment: "No",
  },
  {
    timestamp: "08/07/2020 12:04",
    gender: "Male",
    age: 21,
    course: "EEE",
    year: "Year 2",
    cgpa: "3.00 - 3.49",
    maritalStatus: "No",
    depression: "Yes",
    anxiety: "Yes",
    panicAttack: "No",
    treatment: "Yes",
  },
];

const App = () => {
  const [data, setData] = useState(initialData);
  const [formState, setFormState] = useState({
    timestamp: "",
    gender: "",
    age: "",
    course: "",
    year: "",
    cgpa: "",
    maritalStatus: "",
    depression: "",
    anxiety: "",
    panicAttack: "",
    treatment: "",
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormState({ ...formState, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setData([...data, formState]);
    setFormState({
      timestamp: "",
      gender: "",
      age: "",
      course: "",
      year: "",
      cgpa: "",
      maritalStatus: "",
      depression: "",
      anxiety: "",
      panicAttack: "",
      treatment: "",
    });
  };

  return (
    <div className="container">
      <h1>Student Mental Health Data</h1>

      {/* Data Table */}
      <div className="table-container">
        <table>
          <thead>
            <tr>
              <th>Timestamp</th>
              <th>Gender</th>
              <th>Age</th>
              <th>Course</th>
              <th>Year</th>
              <th>CGPA</th>
              <th>Marital Status</th>
              <th>Depression</th>
              <th>Anxiety</th>
              <th>Panic Attack</th>
              <th>Treatment</th>
            </tr>
          </thead>
          <tbody>
            {data.map((entry, index) => (
              <tr key={index}>
                <td>{entry.timestamp}</td>
                <td>{entry.gender}</td>
                <td>{entry.age}</td>
                <td>{entry.course}</td>
                <td>{entry.year}</td>
                <td>{entry.cgpa}</td>
                <td>{entry.maritalStatus}</td>
                <td>{entry.depression}</td>
                <td>{entry.anxiety}</td>
                <td>{entry.panicAttack}</td>
                <td>{entry.treatment}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Form */}
      <center><h2>Add New Entry</h2></center>
      <form onSubmit={handleSubmit} className="form two-column-form">
        <div className="form-columns">
          <div className="left-column">
            {Object.entries(formState).slice(0, 6).map(([key, value]) => (
              <div key={key} className="form-group">
                <label>
                  {key.charAt(0).toUpperCase() + key.slice(1)}:
                  <input
                    type="text"
                    name={key}
                    value={value}
                    onChange={handleInputChange}
                    required
                  />
                </label>
              </div>
            ))}
          </div>
          <div className="right-column">
            {Object.entries(formState).slice(6).map(([key, value]) => (
              <div key={key} className="form-group">
                <label>
                  {key.charAt(0).toUpperCase() + key.slice(1)}:
                  <input
                    type="text"
                    name={key}
                    value={value}
                    onChange={handleInputChange}
                    required
                  />
                </label>
              </div>
            ))}
          </div>
        </div>
        <center><button type="submit" className="submit-btn">
          Submit
        </button></center>
      </form>
    </div>
  );
};

export default App;
