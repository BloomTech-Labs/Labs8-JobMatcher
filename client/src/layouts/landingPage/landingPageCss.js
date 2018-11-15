import styled from "styled-components";
import { Link } from "react-router-dom";

export const LandingDiv = styled.div`
	width: 100%;
	min-height: 100vh;
	font-size: 16px;
	padding-top: 100px;
	background-image: linear-gradient(
			rgba(74, 74, 74, 0.7),
			rgba(47, 47, 47, 0.7)
		),
		url(../../asset/bg-lg.jpg);
	background-size: cover;
	color: white;
`;
export const CenterDiv = styled.div`
	position: absolute;
	top: 50%;
	left: 50%;
	transform: translate(-50%, -50%);
`;
export const StyledLink = styled(Link)`
	padding: 10px 20px;
	font-size: 16px;
	background-color: #9c17ff;
	color: white;
	margin: 10px;
	border-radius: 10px;
	box-shadow: 0 4px 16px 2px #2e2e2e62;
	transition: all 0.3s;

	&:hover {
		text-decoration: none;
		color: white;
		box-shadow: 0 10px 16px 2px #2e2e2e62;
	}
`;
export const StyledSvg = styled.path`
	fill: #9c17ff;
	stroke: #000990;
	stroke-miterlimit: 10;
	position: absolute;
	bottom: 0;
`;