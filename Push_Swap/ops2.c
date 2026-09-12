/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ops2.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mkhashan <mkhashan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/28 19:29:30 by mkhashan          #+#    #+#             */
/*   Updated: 2026/01/28 19:29:30 by mkhashan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	rx(t_stack *stack_x)
{
	if (!stack_x || !stack_x->head || stack_x->size < 2)
		return ;
	stack_x->head = stack_x->head->next;
	stack_x->rx += 1;
}

void	rr(t_stack *s1, t_stack *s2)
{
	rx(s1);
	rx(s2);
}

void	rrx(t_stack *stack_x)
{
	if (!stack_x || !stack_x->head || stack_x->size < 1)
		return ;
	stack_x->head = stack_x->head->prev;
	stack_x->rrx += 1;
}

void	rrr(t_stack *s1, t_stack *s2)
{
	rrx(s1);
	rrx(s2);
}
