from openerp import tools
from openerp.osv import fields,osv
import openerp.addons.decimal_precision as dp
import time
import logging
from openerp.tools.translate import _

_logger = logging.getLogger(__name__)

class partner(osv.osv):
	_name 		= "res.partner"
	_inherit 	= "res.partner"
	_columns 	= {
		'partner_cash_ids'		: fields.one2many('reliance.partner_cash','partner_id','Cash', ondelete="cascade"),
		'partner_stock_ids'		: fields.one2many('reliance.partner_stock','partner_id','Stock', ondelete="cascade"),
	}
	
	def get_ls_cash(self, cr, uid, cif, context=None):

		pid = self.search(cr, uid, [('cif','=',cif)], context=context)
		partner_cash = self.pool.get('reliance.partner_cash')
		_logger.warning('pid=%s' % pid)
		if pid:
			cashs = partner_cash.search_read(cr,uid,[('partner_id','=',pid[0])],context=context)
		else:
			_logger.error('no partner with cif=%s' % cif)
		return cashs 


	def get_ls_stock(self, cr, uid, cif, context=None):

		pid = self.search(cr, uid, [('cif','=',cif)], context=context)
		partner_stock = self.pool.get('reliance.partner_stock')
		_logger.warning('pid=%s' % pid)
		if pid:
			stocks = partner_stock.search_read(cr,uid,[('partner_id','=',pid[0])],context=context)
		else:
			_logger.error('no partner with cif=%s' % cif)
		return stocks


class partner_cash(osv.osv):
	_name 		= "reliance.partner_cash"
	_rec_name 	= "partner_id"
	_columns 	= {
		"partner_id"	: fields.many2one('res.partner', 'Partner', select=1),
		"client_id"		: fields.related('partner_id', 'cif' , type="char", 
							relation="res.partner", string="Client ID" ),
		"date"			: fields.date("Date"),
		"cash_on_hand"	: fields.float("Cash on Hand"),
		"saldo_t1"		: fields.float("SaldoT1"),
		"saldo_t2"		: fields.float("SaldoT2"),
	}

class partner_stock(osv.osv):
	_name 		= "reliance.partner_stock"
	_rec_name 	= "stock_id"
	_columns 	= {
		"partner_id"		: fields.many2one('res.partner', 'Partner', select=1),
		"date"				: fields.date("Date", select=1),
		"client_id"			: fields.related('partner_id', 'cif' , type="char", 
								relation="res.partner", string="Client ID" ),
		"stock_id"			: fields.char("Stock ID", select=1),
		"stock_name"		: fields.char("Stock Name", select=1),
		"avg_price"			: fields.float("Avg Price"),
		"close_price"		: fields.float("Close Price"),
		"balance"			: fields.float("Balance"),
		"lpp"				: fields.float("LPP"),
		"stock_avg_value"	: fields.float("Stock Avg Value"),
		"market_value"		: fields.float("Market Value"),
		"stock_type"		: fields.char("Stock Type"),
		"sharesperlot"		: fields.char("Shares per Lot"),
	}

