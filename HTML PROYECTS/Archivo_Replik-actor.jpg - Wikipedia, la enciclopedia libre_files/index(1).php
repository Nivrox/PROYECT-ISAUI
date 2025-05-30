/* See [[mw:Reference Tooltips]] */

.rt-overlay {
	position: absolute;
	width: 100%;
	font-size: calc(var(--font-size-medium, 1rem) * (13 / 14));
	line-height: 1.5em;

	/* Remove after https://phabricator.wikimedia.org/T369880 is resolved and $teleportTarget is assigned */
	z-index: 800; /* match z-index-tooltip in https://doc.wikimedia.org/codex/latest/design-tokens/z-index.html */
	top: 0;
}

/* Remove after https://phabricator.wikimedia.org/T369880 is resolved and $teleportTarget is assigned */
.skin-vector-legacy .rt-overlay {
	font-size: 13px;
}

.skin-monobook .rt-overlay {
	font-size: 12.7px;
}

.rt-tooltip {
	position: absolute;
	max-width: 27em;
	background: var(--background-color-base, #fff);
	color: var(--color-base, #202122);
	border: 1px solid var(--border-color-subtle, #c8ccd1);
	border-radius: 2px;
	box-shadow: 0 20px 48px 0 rgba(0, 0, 0, 0.2);
}

html.skin-theme-clientpref-night .rt-tooltip {
	box-shadow: 0 20px 48px 0 rgba(0, 0, 0, 1);
}

/* Extend the tooltip vertically to make sure it doesn't disappear while the user moves the mouse to it */
.rt-tooltip-above .rt-hoverArea {
	margin-bottom: -0.6em;
	padding-bottom: 0.6em;
}

.rt-tooltip-below .rt-hoverArea {
	margin-top: -0.7em;
	padding-top: 0.7em;
}

.rt-scroll {
	overflow-x: auto;
}

.rt-content {
	padding: 0.7em 0.9em;
	overflow-wrap: break-word;
}

.rt-tail {
	/* Use 48%, not 50%, to make the tail start at a right place in Blink browsers in Windows on bigger system font sizes */
	background: linear-gradient(to top right, var(--border-color-subtle, #c8ccd1) 48%, rgba(0, 0, 0, 0) 48%);

	--tail-left: 19px;
	--tail-side-width: 13px;
}

.rt-tail,
.rt-tail:after {
	position: absolute;

	/* Make sure the tail is behind the scrollbar, e.g. [73] at
	   https://en.wikipedia.org/w/index.php?title=Lemniscate_elliptic_functions&oldid=1231701944#cite_ref-73
	   if .rt-tooltip has width of 25em */
	z-index: -1;
	
	width: var(--tail-side-width);
	height: var(--tail-side-width);
}

.rt-tail:after {
	content: '';
	background: var(--background-color-base, #fff);
	bottom: 1px;
	left: 1px;
}

.rt-tooltip-above .rt-tail {
	transform: rotate(-45deg);
	transform-origin: 100% 100%;
	bottom: 0;
	left: var(--tail-left);
}

.rt-tooltip-below .rt-tail {
	transform: rotate(135deg);
	transform-origin: 0 0;
	top: 0;
	left: calc(var(--tail-left) + var(--tail-side-width));
}

.rt-settingsLink {
	background-image: url(data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%2024%2024%22%3E%0D%0A%20%20%20%20%3Cpath%20fill%3D%22%2354595d%22%20d%3D%22M20%2014.5v-2.9l-1.8-.3c-.1-.4-.3-.8-.6-1.4l1.1-1.5-2.1-2.1-1.5%201.1c-.5-.3-1-.5-1.4-.6L13.5%205h-2.9l-.3%201.8c-.5.1-.9.3-1.4.6L7.4%206.3%205.3%208.4l1%201.5c-.3.5-.4.9-.6%201.4l-1.7.2v2.9l1.8.3c.1.5.3.9.6%201.4l-1%201.5%202.1%202.1%201.5-1c.4.2.9.4%201.4.6l.3%201.8h3l.3-1.8c.5-.1.9-.3%201.4-.6l1.5%201.1%202.1-2.1-1.1-1.5c.3-.5.5-1%20.6-1.4l1.5-.3zM12%2016c-1.7%200-3-1.3-3-3s1.3-3%203-3%203%201.3%203%203-1.3%203-3%203z%22%2F%3E%0D%0A%3C%2Fsvg%3E);
	float: right;
	margin: -0.5em -0.5em 0 0.5em;
	box-sizing: border-box;
	height: 32px;
	width: 32px;
	border: 1px solid transparent;
	border-radius: 2px;
	background-position: center center;
	background-repeat: no-repeat;
	background-size: 24px 24px;
}

html.skin-theme-clientpref-night .rt-settingsLink {
	background-image: url(data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%2024%2024%22%3E%0D%0A%20%20%20%20%3Cpath%20fill%3D%22%23c8ccd1%22%20d%3D%22M20%2014.5v-2.9l-1.8-.3c-.1-.4-.3-.8-.6-1.4l1.1-1.5-2.1-2.1-1.5%201.1c-.5-.3-1-.5-1.4-.6L13.5%205h-2.9l-.3%201.8c-.5.1-.9.3-1.4.6L7.4%206.3%205.3%208.4l1%201.5c-.3.5-.4.9-.6%201.4l-1.7.2v2.9l1.8.3c.1.5.3.9.6%201.4l-1%201.5%202.1%202.1%201.5-1c.4.2.9.4%201.4.6l.3%201.8h3l.3-1.8c.5-.1.9-.3%201.4-.6l1.5%201.1%202.1-2.1-1.1-1.5c.3-.5.5-1%20.6-1.4l1.5-.3zM12%2016c-1.7%200-3-1.3-3-3s1.3-3%203-3%203%201.3%203%203-1.3%203-3%203z%22%2F%3E%0D%0A%3C%2Fsvg%3E);
}

.rt-settingsLink:hover,
.rt-settingsLink:active {
	background-color: var(--background-color-interactive, #eaecf0);
}

.rt-settingsLink:active {
	border-color: var(--border-color-interactive, #72777d);
}

.rt-settingsLink:focus {
	outline: 1px solid transparent;
}

.rt-settingsLink:focus:not(:active) {
	border-color: var(--border-color-progressive--focus, #36c);
	box-shadow: inset 0 0 0 1px var(--box-shadow-color-progressive--focus, #36c);
}

.rt-target {
	background-color: var(--background-color-progressive-subtle, #eaf3ff);
}

.rt-enableField {
	font-weight: bold;
	margin-bottom: 1.25em;
}

.rt-numberInput.rt-numberInput {
	width: 10em;
}

.rt-tooltipsForCommentsField.rt-tooltipsForCommentsField.rt-tooltipsForCommentsField {
	margin-top: 1.25em;
}

.rt-disabledHelp {
	border-collapse: collapse;
}

.rt-disabledHelp td {
	padding: 0;
}

.rt-disabledNote.rt-disabledNote {
	vertical-align: bottom;
	padding-left: 0.36em;
	font-weight: bold;
}

@keyframes rt-fade-in-up {
	0% {
		opacity: 0;
		transform: translate(0, 20px);
	}
	100% {
		opacity: 1;
		transform: translate(0, 0);
	}
}

@keyframes rt-fade-in-down {
	0% {
		opacity: 0;
		transform: translate(0, -20px);
	}
	100% {
		opacity: 1;
		transform: translate(0, 0);
	}
}

@keyframes rt-fade-out-down {
	0% {
		opacity: 1;
		transform: translate(0, 0);
	}
	100% {
		opacity: 0;
		transform: translate(0, 20px);
	}
}

@keyframes rt-fade-out-up {
	0% {
		opacity: 1;
		transform: translate(0, 0);
	}
	100% {
		opacity: 0;
		transform: translate(0, -20px);
	}
}

.rt-fade-in-up {
	animation: rt-fade-in-up 0.2s ease forwards;
}

.rt-fade-in-down {
	animation: rt-fade-in-down 0.2s ease forwards;
}

.rt-fade-out-down {
	animation: rt-fade-out-down 0.2s ease forwards;
}

.rt-fade-out-up {
	animation: rt-fade-out-up 0.2s ease forwards;
}