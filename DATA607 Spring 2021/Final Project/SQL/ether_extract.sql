SELECT eb.ether_dt, eb.ether_ts, ep.ether_price, eb.ether_blk_size, et.ether_cnt
FROM ether.ether_block_size eb, ether.ether_price_tbl ep, ether_trans et
where eb.ether_dt = ep.ether_dt
and eb.ether_dt = et.ether_dt
and eb.ether_ts = ep.ether_ts
and eb.ether_ts = et.ether_ts
;