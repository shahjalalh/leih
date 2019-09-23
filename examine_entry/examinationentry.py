from openerp.osv import fields, osv
from openerp.tools.translate import _
from datetime import date, time


class examination_entry(osv.osv):
    _name = "examination.entry"

    _columns = {

        'name': fields.char("Test Name",required=True),
        'group':fields.many2one('diagnosis.group',"Group"),
        'department':fields.char("Department"),
        'rate':fields.integer("Rate"),
        'required_time':fields.char("Required time"),
        'sample_req': fields.boolean("Sample Required"),
        'individual': fields.boolean("Individual"),
        'manual': fields.boolean("Manual"),
        'merge': fields.boolean("Merge"),
        'dependency': fields.boolean("Dependency"),
        'sample_type':fields.many2one('sample.type','Sample Type'),
        'examination_entry_line':fields.one2many('examination.entry.line','examinationentry_id','Parameters')

    }
    def onchange_group(self,cr,uid,ids,group,context=None):

        test={'values':{}}
        dep_object=self.pool.get('diagnosis.group').browse(cr,uid,group,context=None)
        abc={'department':dep_object.department.name}
        test['value']=abc
        # import pdb
        # pdb.set_trace()
        return test


# many2one('leih.doctors',"Test Names", required=True, ondelete='cascade', select=True)

class testentryparamaerte(osv.osv):
    _name = 'examination.entry.line'
    _columns = {

        'name': fields.char("Name",ondelete='cascade'),
        'examinationentry_id': fields.many2one('examination.entry', "Test Entry"),
        'reference_value': fields.char("Reference Value"),
        'others': fields.char("Others")
    }
