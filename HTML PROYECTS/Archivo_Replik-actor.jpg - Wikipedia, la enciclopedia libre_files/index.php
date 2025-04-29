/* CSS placed here is included on the file description page, also included on File-pages of Commons files on the local wikis */
/* Note that there are many non-Wikimedia / non-Wikipedia local wikis as well that use Commons as their repository! */
/* http://www.mediawiki.org/wiki/InstantCommons. Do not assume any language, direction, environment or Skin here. */

/* Hide TOC on file-pages */
.ns-6 #toc { display: none !important; }
 
/* Make {{location}} look like part of the info template */

.commons-file-information-table + table.commons-file-information-table,
.commons-file-information-table + div.commons-file-information-table > table
{
 border-top: 0;
 padding-top: 0;
 margin-top: -8px;
}

/* Used in several license and collection info templates in the File namespace */
/* such as [[Template:PermissionOTRS/layout]] */
.messagebox {
 border: 1px solid #aaa;
 background: var(--background-color-interactive-subtle, #f8f9fa);
 width: 80%;
 margin: 0 auto 1em;
 padding: 0.2em;
 text-align: justify;
}

/* Styling the paramter fields */
.fileinfo-paramfield {
 background: #ccf;
 text-align: right;
 padding-right: 0.4em;
 width: 15%;
 font-weight: bold;
}

/* Move h2 headers in the files description of the parser output
   from left to right for users with RTL interface */
/* @noflip */
body.rtl.ns-6 div.mw-parser-output[dir="ltr"] h2,
body.rtl.ns-6 div.mw-parser-output[dir="ltr"] .mw-heading { direction: rtl; }

/**
 * IMPORTANT:
 *
 * These styles are copied from [[Module:Information/styles.css]].
 * Do not change them without changing that page.
 *
 * See [[Module talk:Information/styles.css]] for details.
 */
/* == BEGIN copy of [[Module:Information/styles.css]] == */
/**
 * Generally we have div.commons-file-information-table > table.fileinfotpl-type-information
 * But additional cells have table.commons-file-information-table
 * We currently only deal with tbody, as there are no known usages of thead/tfoot
 * This is hyper specific to avoid 
 */
table.commons-file-information-table,
.fileinfotpl-type-information,
.fileinfotpl-type-artwork {
	/* toccolours */
	border: 1px solid var(--border-color-base,#a2a9b1);
	background-color: var(--background-color-interactive-subtle,#f8f9fa);
	padding: 5px;
	font-size: 95%;
	/* end of toccolours */
	border-spacing: 2px;
	box-sizing: border-box;
	margin: 0;
	width: 100%;
	color: inherit;
}

table.commons-file-information-table > tbody > tr,
.fileinfotpl-type-information > tbody > tr,
.fileinfotpl-type-artwork > tbody > tr {
	vertical-align: top;
}

table.commons-file-information-table > tbody > tr > td,
table.commons-file-information-table > tbody > tr > th, 
.fileinfotpl-type-information > tbody > tr > td,
.fileinfotpl-type-information > tbody > tr > th,
.fileinfotpl-type-artwork > tbody > tr > td,
.fileinfotpl-type-artwork > tbody > tr > th {
	padding: 4px;
}

/* This should be removed from MediaWiki:Filepage.css and MediaWiki:Common.css */
.fileinfo-paramfield {
	background: #ccf;
	text-align: right;
	padding-right: 0.4em;
	width: 15%;
	font-weight: bold;
	color: inherit;
}

/* stack with additional adjacent templates */
.commons-file-information-table + table.commons-file-information-table,
.commons-file-information-table + div.commons-file-information-table > table {
	border-top: 0;
	padding-top: 0;
	margin-top: -8px;
}

/* Layout on mobile devices */
@media only screen and (max-width:719px) {
	table.commons-file-information-table,
	.commons-file-information-table .fileinfotpl-type-information,
	.commons-file-information-table .fileinfotpl-type-artwork {
		border-spacing: 0;
		padding: 0;
		word-break: break-word;
		width: 100% !important;
	}

	.commons-file-information-table > tbody,
	.fileinfotpl-type-information > tbody,
	.fileinfotpl-type-artwork > tbody {
		display: block;
	}

	.commons-file-information-table > tbody > tr > td,
	.commons-file-information-table > tbody > tr > th,
	.fileinfotpl-type-information > tbody > tr > td,
	.fileinfotpl-type-information > tbody > tr > th,
	.fileinfotpl-type-artwork > tbody > tr > td,
	.fileinfotpl-type-artwork > tbody > tr > th {
		padding: 0.2em 0.4em;
		text-align: left;
		text-align: start;
	}

	.commons-file-information-table > tbody > tr,
	.fileinfotpl-type-information > tbody > tr,
	.fileinfotpl-type-artwork > tbody > tr {
		display: flex;
		flex-direction: column;
	}

	/* stack with additional adjacent templates */
	.commons-file-information-table + table.commons-file-information-table,
	.commons-file-information-table + div.commons-file-information-table > table {
		margin-top: -1px;
	}

	table .fileinfo-paramfield {
		box-sizing: border-box;
		flex: 1 0 100%;
		width: 100%;
	}
}

table.commons-file-information-table, .fileinfotpl-type-information, .fileinfotpl-type-artwork,
.fileinfo-paramfield {
	color: var(--color-base,#202122);
}

/********* General fixes for night mode *********/
html.skin-theme-clientpref-night .fileinfo-paramfield {
	background: #2a2a5c;
	color: white;
}
html.skin-theme-clientpref-night .fileinfotpl-type-artwork tbody > tr > th[style*="#ccf"] {
	background-color: #2a2a5c !important;;	
	color: white;
}

@media screen and (prefers-color-scheme: dark) {
	html.skin-theme-clientpref-os .fileinfo-paramfield {
		background: #2a2a5c;
		color: white;
	}
	html.skin-theme-clientpref-os .fileinfotpl-type-artwork tbody > tr > th[style*="#ccf"] {
		background-color: #2a2a5c !important;;	
		color: white;
	}
}
/* == END copy of [[Module:Information/styles.css]] == */

/**
 * IMPORTANT:
 *
 * These styles are copied from [[Template:Cc-by-sa-layout/styles.css]].
 * Do not change them without changing that page.
 *
 * See [[Module talk:Information/styles.css]] (which is similar) for details.
 */
/* == BEGIN copy of [[Template:Cc-by-sa-layout/styles.css]] == */
.responsive-license-cc {
    clear: both; 
    text-align: center;
    box-sizing: border-box;
    width: 100%;
    justify-content: space-around;
    align-items: center;
    margin: 0.5em auto;
    color: var(--color-base, #202122);
    background-color: var(--background-color-neutral-subtle, #f9f9f9);
    border-width: 2px;
    border-style: solid;
    border-top-color: var(--border-color-subtle, #e0e0e0);
    border-right-color: var(--border-color-subtle, #e0e0e0);
    border-bottom-color: var(--border-color-subtle, #e0e0e0);
    border-left-color: var(--border-color-subtle, #e0e0e0);
    border-spacing: 8px;
    display: flex;
}
.responsive-license-cc div {
	margin: 4px;
}
.rlicense-text div {
	margin: 0.5em auto;
}

@media screen and (max-width: 640px) { /* For mobile devices */
	.responsive-license-cc {
		flex-flow: column;
	}
	.rlicense-text {
		order: 1;
	}
}
/* == END copy of [[Template:Cc-by-sa-layout/styles.css]] == */