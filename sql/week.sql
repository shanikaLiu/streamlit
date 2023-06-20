select
	case when a.sales = '' then null else a.sales end as sales,
	a.id as eiz_account_id,
	a.email,
	a.companyName,
	count( c.id ) as numberOfconsignments,
	sum( c.shippingMethod_price_amount ) as total_spend,
	date_format( date_add( c.created_at, interval - weekday( c.created_at ) + 6 day ), '%Y-%m-%d' ) as week_end
from
	Fulfillments_consignments c
	left join accounts a on c.account_id = a.id 
where
	c.plugin_id in ( 10, 120 ) 
	and c.`status` in ( 2, 3 ) 
	and c.created_at between :start_time
	and :end_time
group by
	c.account_id,
	date_format( date_add( c.created_at, interval - weekday( c.created_at ) + 6 day ), '%Y-%m-%d' ) 
order by
    date_format( date_add( c.created_at, interval - weekday( c.created_at ) + 6 day ), '%Y-%m-%d' ) desc,
    sum( c.shippingMethod_price_amount ) desc