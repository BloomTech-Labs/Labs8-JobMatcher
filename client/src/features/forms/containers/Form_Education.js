import React, { Component } from "react";
import Form from "../components";

class EducationContainer extends Component {
	state = {
		date: {
			id: "education_data",
			date: [new Date(), new Date()]
		},
		school: {
			value: ""
		},
		study: {
			value: ""
		},
		Degree: {
			value: ""
		},
		description: {
			id: "education_description",
			value: ""
		}
	};

	onChange = e => {
		let updateState = { ...this.state };
		if (e.target) {
			updateState[e.target.name].value = e.target.value;
		} else {
			updateState.date.date = e;
		}
		this.setState({ ...updateState });
	};

	render() {
		return (
			<Form
				title="Education"
				onChange={this.onChange}
				state={this.state}
			/>
		);
	}
}

export default EducationContainer;
