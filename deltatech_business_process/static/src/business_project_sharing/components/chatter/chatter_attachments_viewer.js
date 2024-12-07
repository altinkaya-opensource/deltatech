/** @odoo-module */

const {Component} = owl;

export class ChatterAttachmentsViewer extends Component {}

ChatterAttachmentsViewer.template = "deltatech_business_process.ChatterAttachmentsViewer";
ChatterAttachmentsViewer.props = {
    attachments: Array,
    canDelete: {type: Boolean, optional: true},
    delete: {type: Function, optional: true},
};
ChatterAttachmentsViewer.defaultProps = {
    delete: async () => {},
};
